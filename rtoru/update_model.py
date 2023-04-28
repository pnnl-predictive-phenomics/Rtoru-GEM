from memote.suite.cli.reports import diff
import cobra
import os
import logging
from cobra.manipulation.modify import rename_genes
from concerto.utils.biolog_help import add_biolog_exchanges

log = logging.getLogger()

_file_path = os.path.dirname(__file__)
starting_model_f_name = 'Rt_IFO0880.xml'
s_model_path = os.path.join(_file_path, starting_model_f_name)

starting_model = cobra.io.read_sbml_model(s_model_path)
starting_model.id = "RT"

output_model_name = 'Rhodo_Toru.xml'
output_model_path = os.path.join(_file_path, output_model_name)


def write_model(model):
    cobra.io.write_sbml_model(model, output_model_path)


def update_1(model):
    # updates bug in compartment of the model
    log.info("Adding RT to prefix")

    new_names = {}
    for gene in model.genes:
        new_names[gene.id] = f'RT_{gene.id}'
    rename_genes(model, new_names)
    return model


def update_2(model):
    # add missing biolog reactions to model
    log.info("Adding RT to prefix")
    model = add_biolog_exchanges(model)
    return model


def update_model():
    # Fix compartments
    model = update_1(starting_model)
    model = update_2(model)
    write_model(model)


if __name__ == '__main__':
    # update_model()
    model_paths = [s_model_path, output_model_path]
    diff(
        [
            *model_paths,
            '--filename', os.path.join(_file_path, 'model_differences.html'),
            '--experimental', os.path.join(_file_path, 'data', 'experiments.yml'),
            # '--custom-tests', os.path.join(_file_path, 'custom_tests'),
            '--exclusive', 'test_growth',
        ]
    )
