import cobra
import pathlib

path = pathlib.Path(__file__).parent

rt = cobra.io.read_sbml_model(
    path.joinpath('Rhodo_Toru.xml').__str__()
)

exp_file_path = path.joinpath('data', 'experiments.yml').__str__()