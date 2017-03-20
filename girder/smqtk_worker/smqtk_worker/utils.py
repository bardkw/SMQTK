import itertools

from smqtk.utils.image_utils import is_valid_element
from smqtk.utils import parallel
from smqtk.representation.descriptor_index.postgres import PostgresDescriptorIndex
from smqtk.representation.data_element.girder import GirderDataElement

from girder_client import HttpError

from .settings import (DB_HOST, DB_NAME, DB_USER, DB_PASS)


def descriptorIndexFromFolderId(folderId):
    return PostgresDescriptorIndex('descriptor_index_%s' % folderId,
                                   db_name=DB_NAME,
                                   db_host=DB_HOST,
                                   db_user=DB_USER,
                                   db_pass=DB_PASS)


def smqtkileIdFromName(gc, smqtkFolder, name):
    item = list(gc.listItem(smqtkFolder['_id'], name=name))[0]
    return list(gc.listFile(item['_id']))[0]['_id']


def getCreateFolder(gc, parentFolderId, name):
    try:
        # create/reuse existing
        smqtkFolder = gc.createFolder(parentFolderId, name)
    except HttpError:
        smqtkFolder = gc.get('folder', parameters={'parentId': parentFolderId,
                                                   'parentType': 'folder',
                                                   'name': name})[0]

    return smqtkFolder


def createOverwriteItem(gc, parentFolderId, name):
    """
    Creates an item, overwriting it if it already existed.

    :param gc: Instance of GirderClient with the correct permissions.
    :param parentFolderId: The parent folder of the item.
    :param name: The name of the item to create.
    :returns: The newly created item.
    :rtype: dict
    """
    toDelete = gc.listItem(parentFolderId, name=name)

    for item in toDelete:
        gc.delete('item/%s' % item['_id'])

    return gc.createItem(parentFolderId, name)


def initializeItemWithFile(gc, item):
    """
    Initializes an item with an empty file, returning that file.

    :param gc: Instance of GirderClient with the correct permissions.
    :param item: The item (dictionary) to initialize.
    :returns: The newly created file
    :rtype: dict
    """
    return gc.post('/file', {'parentId': item['_id'],
                             'parentType': 'item',
                             'size': 0,
                             'name': item['name']})


def iter_valid_elements(dataElementUris, valid_content_types):
    """
    Find the GirderDataElements which are loadable images and
    valid according to valid_content_types.

    :param dataElementUris: A list of Girder Data Element URIs.
    :param valid_content_types: A list of valid content types, generally
        passed by a descriptor generator.
    :returns: A generator over valid GirderDataElements.
    :rtype: generator
    """
    def is_valid(dataElementUri):
        dfe = GirderDataElement.from_uri(dataElementUri)

        if is_valid_element(dfe,
                            valid_content_types=valid_content_types,
                            check_image=True):
            return dfe
        else:
            return False

    return itertools.ifilter(None, parallel.parallel_map(is_valid,
                                                         dataElementUris,
                                                         use_multiprocessing=False))
