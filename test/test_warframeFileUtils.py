# coding=utf-8
import unittest

from warframeAlert.services.updateFileService import UpdateFileService
from warframeAlert.utils.fileUtils import get_separator, check_file, delete_file
from warframeAlert.utils.warframeFileUtils import translate_sortie_drop, translate_free_roam_drop, \
    translate_relic_drop, translate_mission_drop, translate_key_drop, translate_transient_drop, \
    translate_bp_by_item_drop, translate_bp_by_source_drop, translate_mod_by_item_drop, translate_mod_by_source_drop, \
    decompress_export_manifest_index


class TestWarframeUtils(unittest.TestCase):

    def test_download_all_file(self):
        test_class = UpdateFileService()
        manifest_id = decompress_export_manifest_index()
        test_class.download_export_manifest(manifest_id)

    def test_decompress_export_manifest_index(self):
        manifest_id = decompress_export_manifest_index()
        print(manifest_id)
        self.assertIn("ExportManifest.json!", manifest_id)

    def test_create_sortie_drop(self):
        delete_file("data" + get_separator() + "sortie_it.json")

        translate_sortie_drop()

        self.assertEqual(check_file("sortie_it.json"), True)

    def test_create_freeroam_drop_cetus(self):
        delete_file("data" + get_separator() + "cetus_it.json")

        translate_free_roam_drop("cetus")

        self.assertEqual(check_file("cetus_it.json"), True)

    def test_create_freeroam_drop_fortuna(self):
        delete_file("data" + get_separator() + "fortuna_it.json")

        translate_free_roam_drop("fortuna")

        self.assertEqual(check_file("fortuna_it.json"), True)

    def test_create_freeroam_drop_deimos(self):
        delete_file("data" + get_separator() + "deimos_it.json")

        translate_free_roam_drop("deimos")

        self.assertEqual(check_file("deimos_it.json"), True)

    def test_translate_relic_drop(self):
        delete_file("data" + get_separator() + "relic_it.json")

        translate_relic_drop()

        self.assertEqual(check_file("relic_it.json"), True)

    def test_translate_mission_drop(self):
        delete_file("data" + get_separator() + "mission_it.json")

        translate_mission_drop()

        self.assertEqual(check_file("mission_it.json"), True)

    def test_translate_key_drop(self):
        delete_file("data" + get_separator() + "key_it.json")

        translate_key_drop()

        self.assertEqual(check_file("key_it.json"), True)

    def test_translate_transient_drop(self):
        delete_file("data" + get_separator() + "transient_it.json")

        translate_transient_drop()

        self.assertEqual(check_file("transient_it.json"), True)

    def test_translate_bp_by_item_drop(self):
        delete_file("data" + get_separator() + "bp_by_item_it.json")

        translate_bp_by_item_drop()

        self.assertEqual(check_file("bp_by_item_it.json"), True)

    def test_translate_bp_by_source_drop(self):
        delete_file("data" + get_separator() + "bp_by_source_it.json")

        translate_bp_by_source_drop()

        self.assertEqual(check_file("bp_by_source_it.json"), True)

    def test_translate_mod_by_item_drop(self):
        delete_file("data" + get_separator() + "mod_by_item_it.json")

        translate_mod_by_item_drop()

        self.assertEqual(check_file("mod_by_item_it.json"), True)

    def test_translate_mod_by_source_drop(self):
        delete_file("data" + get_separator() + "mod_by_source_it.json")

        translate_mod_by_source_drop()

        self.assertEqual(check_file("mod_by_source_it.json"), True)

