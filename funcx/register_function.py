from funcx import FuncXClient
from tar import create_tar

fxc = FuncXClient()
function_id = fxc.register_function(create_tar)
print(function_id)
