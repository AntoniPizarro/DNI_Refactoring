from DNI import DNI

def test_function():
    assert DNI.function(False) == "Tus muertos"
    assert DNI.function(2) == "Tus muertos"
    assert DNI.function("ase") == "Tus muertos"
    assert DNI.function([]) == "Tus muertos"
    assert DNI.function(True) == True

def test_get_nums():
    assert DNI("45186457J").get_num() == "45186457"
    assert DNI("btgh5w476w45tg").get_num() == "DNI format incorrect."
    assert DNI("dfgsb").get_num() == "DNI format incorrect."
    assert DNI("4g5186457J").get_num() == "DNI format incorrect."
    assert DNI("").get_num() == "DNI format incorrect."