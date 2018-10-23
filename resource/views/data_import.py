from django.shortcuts import HttpResponse
from resource.utils.ResManager import res_manager
from resource.models.wdf import WDF
from resource.models.character import *
from resource.models.shape import *
from resource.models.monster import Monster, MonsterAction


def wdf_import(request):
    wdf = WDF.objects.get(name="shape.wd3")
    was_list = []
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
    from resource.models.mount import MountAction, Mount
    from resource.models.character import CharacterMount
    cms = CharacterMount.objects.all()

    for cm in cms:
        race = cm.character.race
        m = Mount.objects.get(race=race, level=cm.level)

        was = cm.was
        character = cm.character

        new_ma = MountAction()
        new_ma.mount = m
        new_ma.character = character
        new_ma.was = was
        new_ma.name = cm.name
        new_ma.name_cn = cm.name_cn
        new_ma.save()

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