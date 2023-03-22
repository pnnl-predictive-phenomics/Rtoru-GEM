import cobra
import pathlib
import pandas as pd


path = pathlib.Path(__file__).parent

rt = cobra.io.read_sbml_model(
    path.joinpath('Rhodo_Toru.xml').__str__()
)

exp_file_path = path.joinpath('data', 'experiments.yml').__str__()
expected_metab = pd.read_csv(
    path.joinpath('data', 'excreted_rt.csv').__str__(),
    index_col=0,

).bigg_id