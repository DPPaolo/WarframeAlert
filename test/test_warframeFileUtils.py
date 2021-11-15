# coding=utf-8
from warframeAlert.utils.fileUtils import get_separator, check_file, delete_file
from warframeAlert.utils.warframeFileUtils import translate_sortie_drop, translate_free_roam_drop, \
    translate_relic_drop, translate_mission_drop, translate_key_drop, translate_transient_drop, \
    translate_bp_by_item_drop, translate_bp_by_source_drop, translate_mod_by_item_drop, translate_mod_by_source_drop


class TestWarframeUtils():

    def test_create_sortie_drop(self) -> None:
        delete_file("data" + get_separator() + "sortie_it.json")
        translate_sortie_drop()
        assert check_file("sortie_it.json")

    def test_create_freeroam_drop_cetus(self) -> None:
        delete_file("data" + get_separator() + "cetus_it.json")
        translate_free_roam_drop("cetus")
        assert check_file("cetus_it.json")

    def test_create_freeroam_drop_fortuna(self) -> None:
        delete_file("data" + get_separator() + "fortuna_it.json")
        translate_free_roam_drop("fortuna")
        assert check_file("fortuna_it.json")

    def test_create_freeroam_drop_deimos(self) -> None:
        delete_file("data" + get_separator() + "deimos_it.json")
        translate_free_roam_drop("deimos")
        assert check_file("deimos_it.json")

    def test_translate_relic_drop(self) -> None:
        delete_file("data" + get_separator() + "relic_it.json")
        translate_relic_drop()
        assert check_file("relic_it.json")

    def test_translate_mission_drop(self) -> None:
        delete_file("data" + get_separator() + "mission_it.json")
        translate_mission_drop()
        assert check_file("mission_it.json")

    def test_translate_key_drop(self) -> None:
        delete_file("data" + get_separator() + "key_it.json")
        translate_key_drop()
        assert check_file("key_it.json")

    def test_translate_transient_drop(self) -> None:
        delete_file("data" + get_separator() + "transient_it.json")
        translate_transient_drop()
        assert check_file("transient_it.json")

    def test_translate_bp_by_item_drop(self) -> None:
        delete_file("data" + get_separator() + "bp_by_item_it.json")
        translate_bp_by_item_drop()
        assert check_file("bp_by_item_it.json")

    def test_translate_bp_by_source_drop(self) -> None:
        delete_file("data" + get_separator() + "bp_by_source_it.json")
        translate_bp_by_source_drop()
        assert check_file("bp_by_source_it.json")

    def test_translate_mod_by_item_drop(self) -> None:
        delete_file("data" + get_separator() + "mod_by_item_it.json")
        translate_mod_by_item_drop()
        assert check_file("mod_by_item_it.json")

    def test_translate_mod_by_source_drop(self) -> None:
        delete_file("data" + get_separator() + "mod_by_source_it.json")
        translate_mod_by_source_drop()
        assert check_file("mod_by_source_it.json")
