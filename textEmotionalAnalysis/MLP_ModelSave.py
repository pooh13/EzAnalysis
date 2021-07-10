import tensorflow as tf
import createFolder


def MLP_ModelSave(model):

    path = ('/Models/MLP_Model/')
    createdPath = createFolder.createFolder(path)

    tf.saved_model.save(model, createdPath)
