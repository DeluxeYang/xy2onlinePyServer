from django.shortcuts import HttpResponse
from resource.utils.ResManager import res_manager
from resource.models.wdf import WDF
from resource.models.character import *
from resource.models.shape import *
from resource.models.monster import Monster, MonsterAction


def wdf_import(request):
    wdf = WDF.objects.get(name="gires2.wdf")
    was_list = ['0xB71F1EE2', '0xB7C4D153', '0xB7F391E9', '0xB82AEEAE', '0xB90107F1', '0xB98E8D5A', '0xB99F38DC', '0xB9D07413', '0xBA7549E4', '0xBAF291BD', '0xBBAA9BD4', '0xBC4E3ECB', '0xBC529913', '0xBC87447F', '0xBCC3B06A', '0xBCCCDD0A', '0xBD566902', '0xBEA7091A', '0xBEDBAC88', '0xBF1CB476', '0xBF5B402D', '0xBF69FAC0', '0xBF9B76BF', '0xBFBE1987', '0xBFEEB271', '0xC0137A29', '0xC0140A9A', '0xC02A6AD4', '0xC08AC85E', '0xC14B2691', '0xC1628785', '0xC19EBC1F', '0xC1B0D98A', '0xC1DB12BF', '0xC2BECD6C', '0xC2C6E7CC', '0xC3622E6B', '0xC39E1E0C', '0xC3E7E556', '0xC4C67D05', '0xC4D524A7', '0xC6475A6C', '0xC69361BC', '0xC6ABBAD3', '0xC6B76BB1', '0xC71B90A6', '0xC8824DB6', '0xC9D679C1', '0xCA02FC0A', '0xCA2E2C33', '0xCA7D8BEC', '0xCA8826F9', '0xCA9176B9', '0xCAD50AF0', '0xCB250B45', '0xCB42188E', '0xCB73AC69', '0xCBC7BBB8', '0xCBF8CE8A', '0xCC01E14B', '0xCC5A509F', '0xCC74348A', '0xCC8365F7', '0xCCB4434F', '0xCCF65D7A', '0xCD205AA4', '0xCDD1C341', '0xCDFD26F3', '0xCE18BE9D', '0xCE77A71A', '0xCEB744B5', '0xCEB882CE', '0xCF03B1C1', '0xCF2CDF88', '0xCF4E5266', '0xCF8C009B', '0xD00354F8', '0xD020990A', '0xD1073611', '0xD121EAEE', '0xD139A8FE', '0xD185A9D3', '0xD1A6077C', '0xD1A68BAF', '0xD1DE5B23', '0xD1EFD52C', '0xD2017A6C', '0xD20F1322', '0xD26C2E97', '0xD2CC0C61', '0xD31B21B9', '0xD379AF11', '0xD37A8938', '0xD411DE28', '0xD4146CBA', '0xD43940E0', '0xD46384AD', '0xD46E8931', '0xD4DA2146', '0xD576A7B0', '0xD5AEB0E3', '0xD5C56DDF', '0xD679CB60', '0xD6BE44C1', '0xD7272512', '0xD752FBF5', '0xD78901DB', '0xD7940201', '0xD796CD42', '0xD8496621', '0xD856A233', '0xD858A541', '0xD8E7F6AF', '0xD980A2BE', '0xD982768B', '0xD99484E6', '0xD9A04DA7', '0xD9E0400F', '0xDA25EC3D', '0xDA985AB4', '0xDAA034ED', '0xDD3838ED', '0xDDB867F8', '0xDDE1B981', '0xDEC75822', '0xDED20D7F', '0xDEF70372', '0xDFEEC20D', '0xDFFDC3BE', '0xE09A84F7', '0xE09D4CEE', '0xE0EC8308', '0xE11B594E', '0xE15EF917', '0xE2AA1D28', '0xE2AD4A47', '0xE2F6C302', '0xE2F95A59', '0xE3281032', '0xE36AAE0D', '0xE3DDE6F5', '0xE4377089', '0xE4993261', '0xE4DFAC94', '0xE5041E55', '0xE5125F4B', '0xE5D32BC1', '0xE5E37410', '0xE6491DD3', '0xE66547D1', '0xE75DF40F', '0xE767D7BA', '0xE7914004', '0xE7BDA157', '0xE8005277', '0xE8192240', '0xE8847FA1', '0xE8FD733B', '0xE95B03E5', '0xE962BC78', '0xE96E7CCB', '0xE973F836', '0xE994553E', '0xE9CB6906', '0xEA1D3980', '0xEA65DC26', '0xEA963782', '0xEAC9664B', '0xEAD167C3', '0xEAD9E3FA', '0xEB1B0594', '0xEB1DD01C', '0xEB279C62', '0xEBD05656', '0xEC61451C', '0xEC80637A', '0xEC872EC1', '0xECA78CC7', '0xECC4479D', '0xECD57D14', '0xED1A2D9B', '0xED3E580E', '0xEDEDE96D', '0xEE392F63', '0xEE3DFDA3', '0xEE9BFE83', '0xEEA4F919', '0xEEDC7886', '0xEF61B5B8', '0xEF745009', '0xF00FF1BD', '0xF02440FE', '0xF090A4BB', '0xF0DD31DD', '0xF0F9F338', '0xF11233BB', '0xF16D2CA4', '0xF17BC3D9', '0xF183719A', '0xF1E066FF', '0xF2118F60', '0xF2183114', '0xF221A4EF', '0xF2C0924F', '0xF37FDB9D', '0xF3B62532', '0xF3D4EC1A', '0xF3DEFFE7', '0xF5247F74', '0xF52591B3', '0xF591D605', '0xF5B8E062', '0xF615DBC2', '0xF6C51F02', '0xF6C8DBD0', '0xF6FFA6EC', '0xF735AF74', '0xF73CD42A', '0xF73EAD7A', '0xF7426640', '0xF769EEF2', '0xF7C9CC1C', '0xF86D024B', '0xF8B0B20E', '0xF933D8B8', '0xF9838BCA', '0xF9E27E6E', '0xFA4B00C5', '0xFA5F00D2', '0xFACC038E', '0xFAF67962', '0xFB37229D', '0xFB8DB8AB', '0xFBA7A7FF', '0xFC5444FD', '0xFC849F13', '0xFD2B1B58', '0xFD370DED', '0xFD625FAA', '0xFDA33820', '0xFDBB0AEB', '0xFDBB2611', '0xFED3E499', '0xFF0B1599', '0xFF40DFF7', '0xFF4433E4', '0xFF5A3DD9', '0xFF997CF6']
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
    wdf = WDF.objects.get(name="gires2.wdf")
    was_list = res_manager.get_wdf_file_list(wdf.name)
    print(was_list)
    return HttpResponse("success!")


def task(request):

    return HttpResponse("success!")


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