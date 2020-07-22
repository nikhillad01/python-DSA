import operator
from functools import reduce

TREE = {

    "threshold": 5,
    "variable": "x",
    "operator": ">",
    "left": {
        "variable": "y",
        "threshold": 5,
        "operator": ">",
        "left": {
            "value": "A"
        },
        "right": {
            "variable": "z",
            "operator": "<",
            "threshold": 15,
            "left": {
                "value": "B"
            },
            "right": {
                "value": "C"
            },
            "value": ""
        },
        "value": "",
    },

    "right": {
        "variable": "z",
        "operator": ">",
        "threshold": 5,
        "left": {
            "value": "D"
        },
        "right": {
            "value": "E"
        },
        "value": ""
    }

}


def get_direction(operator_sign, threshold, variable):
    """ Returns next path move left or right according to conditions and values passed
    @params : operator_sign = Comparision operator to check < or >
              threshold  = value to  be compare with given variable value
              variable = actual variable
    """
    if operator_sign == ">":
        if variable > threshold:
            return "left"
        else:
            return "right"
    elif operator_sign == "<":
        if variable < threshold:
            return "left"
        else:
            return "right"


def has_keys(obj):
    """ Checks if Object contains specific keys or not """
    try:
        keys = ['threshold', 'variable']
        for i in keys:
            if not obj[i]:
                return False
        return True
    except Exception:
        return False


def return_json(graph, path):
    """ Returns Json Sub dict from given Tree and List containing visited elements as path """
    try:
        return reduce(operator.getitem, path, graph)
    except Exception:
        return False


def get_op_node(input_dict):
    """ Return output node from given tree
        Traverse the given tree with the conditions from tree
        @params:
                json_tree: Json tree data structure
    """
    current_path = []
    path = get_direction(TREE['operator'], TREE['threshold'], input_dict[TREE['variable']])
    current_path.append(path)  # appends path
    path = return_json(TREE, current_path)
    while not path['value']:
        if has_keys(path):
            move_direction = get_direction(path['operator'], path['threshold'], input_dict[path['variable']])
            current_path.append(move_directio   n)
            path = return_json(TREE, current_path)

    return path['value']


input_dict = {"x": 0, "y": 4, "z": 1}
print(get_op_node(input_dict))
