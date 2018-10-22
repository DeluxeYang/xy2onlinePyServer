from django.shortcuts import HttpResponse
from resource.utils.ResManager import res_manager
from resource.models.wdf import WDF
from resource.models.character import *
from resource.models.shape import *
from resource.models.monster import Monster, MonsterAction


def wdf_import(request):
    wdf = WDF.objects.get(name="shape.wd3")
    was_list = ['0x00833F8C', '0x03B25F45', '0x0BE03DE9', '0x0C4BE170', '0x0D6CC62A', '0x0E6FB012', '0x11B34BD5', '0x17104057', '0x198E4BC5', '0x22EEF045', '0x2AC52D3C', '0x2DCBEA7A', '0x33E185D8', '0x3490392B', '0x3555EECF', '0x40198B61', '0x405C8871', '0x409D1344', '0x42D7F6AA', '0x44EB5896', '0x4564893B', '0x4739BAB8', '0x491226CB', '0x49230666', '0x49B62A4E', '0x4AC9F708', '0x4BA4C1EC', '0x52E0BE5E', '0x53F40676', '0x578497BB', '0x5B84CBC9', '0x5DCEEF82', '0x652DE574', '0x68C23C4B', '0x698D636D', '0x6D0BF1CE', '0x70412D17', '0x759F5D4B', '0x78281CAC', '0x7BC18EB0', '0x7C5A34B7', '0x81E10935', '0x865C569F', '0x86B786ED', '0x88E164E1', '0x8919D042', '0x8AAED2E8', '0x8AEFD825', '0x8F2D1EED', '0x8FACC48D', '0x9ABB5596', '0x9F776D40', '0x9F7D2E44', '0xA7EE46EF', '0xA8656175', '0xA9EB10A7', '0xAD802E0F', '0xAE3F0A96', '0xAE72D16C', '0xAF22F5C3', '0xAFF5E378', '0xB173F939', '0xB3E3FD5B', '0xB5D7620A', '0xB922FABC', '0xBA50D925', '0xBCF47B21', '0xBE464DC8', '0xC1797400', '0xC2E456F5', '0xC33D3EAB', '0xC38DA3CA', '0xC4C5611F', '0xC8F47E57', '0xCB4F7471', '0xCB7E6AA7', '0xCEF93076', '0xD036D599', '0xD44DB088', '0xD4730F32', '0xD92E7941', '0xDBD9B642', '0xDE07BF69', '0xDE21BBE0', '0xDF0046CF', '0xDF992FD9', '0xE000BCF4', '0xF1994024', '0xF5BF7064', '0xF5DD31BC', '0xF683CE35', '0xF6913E71', '0xF75D9AE6', '0xF7BF4054', '0xF80149B8', '0xFFC7B1FE']
    count = 0
    for _hash in was_list:
        was = WAS()
        was.wdf = wdf
        was.hash = _hash
        flag = was.save_with_file()
        if flag:
            count += 1
    return HttpResponse(str(len(was_list)) + "success!" + str(count))


def get_was_list(request):
    wdf = WDF.objects.get(name="shape.wd3")
    was_list = res_manager.get_wdf_file_list(wdf.name)
    print(was_list)
    return HttpResponse("success!")


def task(request):
    _list = ShapeAction.objects.filter(name="jag")
    for action in _list:
        action.name = "jog"
        action.save()
        action.was.describe = action.shape.name_cn + ": " + action.name
        action.was.save()
    return HttpResponse("success!")


def symbolic_animal_import(request):
    from .data.symbolic_animal_data import data
    from resource.models.symbolic_animals import SymbolicAnimal, SymbolicAnimalAction
    for shape_name in data:
        symbolic_animal = SymbolicAnimal()
        symbolic_animal.name = shape_name
        symbolic_animal.name_cn = data[shape_name]["name"]
        symbolic_animal.save()
        for action_name in ["run", "stand"]:
            action = data[shape_name][action_name]
            if action[0] == "":
                continue
            try:
                wdf = WDF.objects.get(name=action[0])
                was = WAS.objects.get(wdf=wdf, hash=action[1])
            except Exception as e:
                print(e, shape_name, action_name)
                continue
            shape_action = SymbolicAnimalAction()
            shape_action.shape = symbolic_animal
            shape_action.was = was
            shape_action.name = action_name
            shape_action.save()

            was.hooked = True
            was.describe = data[shape_name]["name"] + ":" + action_name
            was.save()
    return HttpResponse("success!")


def shape_import(request):
    # from .data.npc_data import NPC
    # from resource.models.shape import Shape, ShapeAction
    # for shape_name in NPC:
    #     keys = list(NPC[shape_name].keys())
    #
    #     new_shape = Shape.objects.get(name=shape_name)
    #
    #     keys.remove("name")
    #
    #     for action_name in keys:
    #         action = NPC[shape_name][action_name]
    #         if action[0] == "":
    #             continue
    #         try:
    #             wdf = WDF.objects.get(name=action[0])
    #             was = WAS.objects.get(wdf=wdf, hash=action[1])
    #         except Exception as e:
    #             print(e, shape_name, action_name)
    #             continue
    #         shape_action = ShapeAction()
    #         shape_action.shape = new_shape
    #         shape_action.was = was
    #         shape_action.name = action_name
    #         shape_action.save()
    #
    #         was.hooked = True
    #         was.describe = NPC[shape_name]["name"] + ":" + action_name
    #         was.save()
    #
    #     print(keys)
    return HttpResponse("success!")


def monster_import(request):
    # from .data.monsters_data import monsters
    # for monster_name in monsters:
    #     monster = monsters[monster_name]
    #
    #     monster_model = Monster()
    #     monster_model.name = monster_name
    #     monster_model.name_cn = monster["name"]
    #     monster_model.title_level = monster["title_level"]
    #     monster_model.init_max_hp = monster["HP"]
    #     monster_model.init_max_mp = monster["MP"]
    #     monster_model.init_max_ap = monster["AP"]
    #     monster_model.init_max_sp = monster["SP"]
    #     monster_model.init_max_speed = monster["speed"]
    #     monster_model.init_max_growth = monster["growth"]
    #     monster_model.init_max_high_growth = monster["high_growth"]
    #
    #     monster_model.gold = monster["gold"]
    #     monster_model.wood = monster["wood"]
    #     monster_model.soil = monster["soil"]
    #     monster_model.water = monster["water"]
    #     monster_model.fire = monster["fire"]
    #     monster_model.save()
    #
    #     for action_name in ["run", "stand", "walk", "attack", "beaten", "defence", "magic", "beaten_down", "static"]:
    #         action = monster[action_name]
    #         wdf = action[0]
    #         _hash = action[1]
    #         if wdf == "":
    #             continue
    #         wdf_model = WDF.objects.get(name=wdf)
    #         try:
    #             was_model = WAS.objects.get(wdf=wdf_model, hash=_hash)
    #         except Exception as e:
    #             print(e)
    #             print(monster_name, action_name, "@@@@@", _hash, )
    #             continue
    #         monster_action = MonsterAction()
    #         monster_action.name = action_name
    #         monster_action.monster = monster_model
    #         monster_action.was = was_model
    #         monster_action.save()
    #
    #         was_model.hooked = True
    #         was_model.describe = monster_model.name_cn + ": " + action_name
    #         was_model.update()

    return HttpResponse("success!")


def character_import(request):
    # from .data.characters_data import characters
    # for race_name in characters:
    #     for character_name in characters[race_name]:
    #         character_info = characters[race_name][character_name]
    #
    #         race = Race.objects.get(name=race_name)
    #         new_character = Character()
    #         new_character.race = race
    #         new_character.name = character_name
    #         new_character.name_cn = character_info["name"]
    #         new_character.gender = -1 if character_info["gender"] == 0 else 1
    #         new_character.describe = character_info["describe"]
    #         new_character.save()
    #         for action_name in ["run", "stand", "stand_tease", "walk"]:
    #             try:
    #                 new_action = CharacterAction()
    #                 new_action.character = new_character
    #                 new_action.name = action_name
    #
    #                 action = character_info[action_name]
    #
    #                 wdf = WDF.objects.get(name=action[0])
    #                 was = WAS.objects.get(wdf=wdf, hash=action[1])
    #                 was.hooked = True
    #                 was.describe = character_info["name"] + ": " + action_name
    #                 was.update()
    #
    #                 new_action.was = was
    #                 new_action.save()
    #             except Exception as e:
    #                 print(e)
    #
    #         for weapon_name in character_info["weapon"]:
    #             for action_name in character_info["weapon"][weapon_name]:
    #                 try:
    #                     new_action = CharacterAction()
    #                     new_action.character = new_character
    #                     new_action.name = action_name
    #                     new_action.weapon = weapon_name
    #
    #                     action = character_info["weapon"][weapon_name][action_name]
    #
    #                     wdf = WDF.objects.get(name=action[0])
    #                     was = WAS.objects.get(wdf=wdf, hash=action[1])
    #                     was.hooked = True
    #                     was.describe = character_info["name"] + ": " + action_name
    #                     was.update()
    #
    #                     new_action.was = was
    #                     new_action.save()
    #                 except Exception as e:
    #                     print(e)

    return HttpResponse("success!")