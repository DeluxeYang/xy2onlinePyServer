from django.shortcuts import HttpResponse
from resource.utils.ResManager import res_manager
from resource.models.wdf import WDF
from resource.models.character import *
from resource.models.shape import *
from resource.models.monster import Monster, MonsterAction
from game.game_server import game_server


def wdf_import(request):
    wdf = WDF.objects.get(name="mapani.wdf")
    was_list = ['0x094AB2FC', '0x1334CAD0', '0x139AF9A1', '0x25F3D0AD', '0x27BBE427', '0x34C534A7', '0x34DB7D2B', '0x364210AA', '0x3E90B7BF', '0x41938E3B', '0x42A1692C', '0x489E1E81', '0x4A590579', '0x514683E8', '0x5222AB97', '0x5702BC05', '0x5CACCB0D', '0x5E1D7FC1', '0x693F0C48', '0x6EF98F77', '0x7C4BF81C', '0x7FC046F6', '0x84FDA92E', '0x8D30C958', '0x9024B224', '0x946F032B', '0x9A1EB8FD', '0x9F24FF04', '0xA1BC1B65', '0xA600EFDF', '0xAC4E1618', '0xB0860891', '0xC0570C07', '0xC20548B2', '0xD1009268', '0xD16C71DF', '0xD334F4F8', '0xD35FED9B', '0xD39F7F26', '0xD3D52AA0', '0xE1976B34', '0xE4CC98F6', '0xEA107BDD', '0xEE9CCF28', '0xF1B48F86', '0xF434D6A1']
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
    wdf = WDF.objects.get(name="mapani.wdf")
    was_list = res_manager.get_wdf_file_list(wdf.name)
    print(was_list)
    return HttpResponse("success!")


def task(request):
    send_data = {'action': "refresh_scene"}
    game_server.broadcast(send_data, except_myself="")
    return HttpResponse(send_data)


def import_character_photo(request):
    from resource.models.character import CharacterPhoto
    from xy2onlineServer.settings import STATIC_URL
    from PIL import Image
    for cn in []:
        wdf = WDF.objects.get(name="photo.wdf")
        photos = WAS.objects.filter(wdf=wdf, describe=cn)
        list_by_size = []
        for photo in photos:
            im = Image.open("static/" + str(photo.image))
            list_by_size.append((im.size[0] * im.size[1], photo, im.size[0], im.size[1]))
        list_by_size.sort(key=lambda x: x[0])
        character = Character.objects.get(name_cn=cn)
        level = 1
        for photo in list_by_size:
            cp = CharacterPhoto()
            cp.character = character
            cp.was = photo[1]
            cp.level = level
            cp.name = str(level)
            cp.name_cn = cn + ": " + str(level)
            level += 1
            cp.w = photo[2]
            cp.h = photo[3]
            cp.save()
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