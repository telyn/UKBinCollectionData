import os
import pytest
import glob
from uk_bin_collection.uk_bin_collection.collect_data import get_council_module
import features.steps.step_helpers.file_handler

@pytest.fixture
def common_schema():
    return file_handler.load_schema_file(f"{context.council}.schema")

base = os.path.dirname(__file__)
output_files = glob(os.join(base, "outputs", "*.json"))

assert len(outputs) > 1

@pytest.fixture(params=[output_files])
def council_output_json(noncommon_output_file):
    with open(noncommon_output_file.param) as f:
        data = json.loads(f)
        return { "filename": noncommon_output_file.param, "obj": data }

# would love to find a way to make multiple instances of this test function automatically

def test_outputs_match_schemas(council_output_json):
    filename = os.path.dirname(council_output_json).
    council_class = get_council_module()
    counc

            common_output = council_class.transform_to_common_output(data)
            common_json = json.dumps(common_output)

            schema_result = file_handler.validate_json_schema(
                common_json, council_schema
            )
            assert schema_result is True


