SIZES = [
    {
        "id": 1,
        "caretes": .5,
        "price": 405
    },
    {
        "id": 2,
        "caretes": .75,
        "price": 782
    }, {
        "id": 3,
        "caretes": 1,
        "price": 1470
    }, {
        "id": 4,
        "caretes": 1.5,
        "price": 1997
    }, {
        "id": 5,
        "caretes": 2,
        "price": 3638
    },
]


def get_all_sizes():
    return SIZES


def get_single_size(id):
    requested_size = None
    for size in SIZES:
        if size["id"] == id:
            requested_size = size
    return requested_size

def create_size(size):
    max_id = SIZES[-1]["id"]
    new_id = max_id + 1
    size["id"] = new_id
    SIZES.append(size)

    return size