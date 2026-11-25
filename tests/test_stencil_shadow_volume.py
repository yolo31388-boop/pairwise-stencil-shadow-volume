import pytest
import graphics.stencil_shadow_volume as mod

CASES = [
    ("clean_nonmanifold", (1,)),
    ("flip_by_camera_side", (1,)),
    ("clear_per_light", (1,)),
    ("extrude_by_light_dist", (1,)),
    ("transparent_separate", (1,)),
    ("shadow_edge_check", (1,)),
    ("load", (1,)),
    ("extrude", (1,)),
    ("stencil", (1,)),
    ("present", (1,)),
    ("validate_stencil", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
