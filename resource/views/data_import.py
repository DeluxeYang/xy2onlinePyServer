from django.shortcuts import HttpResponse
from resource.utils.ResManager import res_manager
from resource.models.wdf import WDF
from resource.models.character import *
from resource.models.shape import *
from resource.models.monster import Monster, MonsterAction


def wdf_import(request):
    wdf = WDF.objects.get(name="photo.wdf")
    was_list = ['0x004E3215', '0x007E89B8', '0x00A92117', '0x01FFFBFA', '0x03A81484', '0x05CD19DA', '0x0677BDB2', '0x0781BE3A', '0x0846F3D5', '0x08CE5122', '0x09193986', '0x099F0A4E', '0x0C05DBFD', '0x0D0FC56C', '0x0F7D958C', '0x108D5BEA', '0x1200391E', '0x1287ACBC', '0x132CF23C', '0x1465706A', '0x14942085', '0x1550BCF2', '0x18A47555', '0x190AB112', '0x19AB25D5', '0x1A105271', '0x1A3AE9C5', '0x1A65146C', '0x1C476132', '0x1D3D7CF9', '0x1D4B2F6D', '0x1D87887C', '0x1EC9887C', '0x1F16B564', '0x2067DC00', '0x20A980C8', '0x20BD7629', '0x20BF744F', '0x2143D71F', '0x217FCDF9', '0x230DFCDD', '0x2381820C', '0x23F50F01', '0x2411FA16', '0x25144015', '0x2976D4FA', '0x2981A65A', '0x2B1E3F8C', '0x2C0AE505', '0x2EC00AA5', '0x2F308EEF', '0x2F694A3F', '0x30661387', '0x3076FC60', '0x308E32FD', '0x31B160DA', '0x334DBA84', '0x338F6548', '0x35C4FF06', '0x372FA153', '0x37412DB2', '0x37614D70', '0x38F6D853', '0x3939BBC0', '0x397FDA0C', '0x39DAB432', '0x3A1EE79A', '0x3BAE8623', '0x3BB12A28', '0x3CB482F9', '0x3D7C56D0', '0x3EEC92A5', '0x3EFD9C60', '0x3F986D95', '0x403149DC', '0x4160682D', '0x417F7D92', '0x44886F96', '0x455E9B25', '0x463692C8', '0x47872EC0', '0x492F144A', '0x4A5AB31D', '0x4BB1E89A', '0x4C2A1465', '0x4C6D73C9', '0x4E86E963', '0x4F97F014', '0x4FF13046', '0x502CE092', '0x525D944C', '0x52F32998', '0x548D02DE', '0x55309D9C', '0x5763727F', '0x58AD76AA', '0x590E8566', '0x5A67D940', '0x5AE145E5', '0x5AF0A410', '0x5B947959', '0x5BE27D29', '0x5C6DCFF7', '0x5C7F1E38', '0x5D8E5BAF', '0x5E1D7FC1', '0x5F0C5562', '0x5FDAAF6A', '0x62CBD7A9', '0x6304C0EA', '0x638A26F4', '0x63FC128B', '0x642B914D', '0x6450AA81', '0x64A489BB', '0x65D1FE04', '0x6650A5E6', '0x66716917', '0x6697E555', '0x6778E030', '0x6825A231', '0x6983ACB7', '0x69D4128E', '0x6A3FC0BE', '0x6C5D9B16', '0x6C76FA3D', '0x6C927D9A', '0x6D05F189', '0x6DD9F1AD', '0x6EA20A36', '0x6EA2FF65', '0x702391B9', '0x71EF98CF', '0x72010B54', '0x72414A81', '0x7254F74E', '0x732D933C', '0x734C19AB', '0x73E42300', '0x74613EF5', '0x74746B9D', '0x747B5BB0', '0x75335E4E', '0x781C7DAA', '0x790EBADA', '0x79D4DB8D', '0x7B27BA25', '0x7BA2C3F8', '0x7BC0EA96', '0x7C5EC587', '0x7D05B4CE', '0x7E63637D', '0x818B924B', '0x822A262B', '0x83DEDB1B', '0x87C0C8B4', '0x8A023ECD', '0x8A6D8DF8', '0x8B0B3D9C', '0x8BEAF382', '0x8C240BFB', '0x8C7BF755', '0x8CABDCB6', '0x8FB719C2', '0x8FEB00CA', '0x905E159B', '0x9178D667', '0x922557A9', '0x94142B6E', '0x942151A8', '0x94DB04CC', '0x94EB6857', '0x9580F606', '0x976DEBB5', '0x976E908E', '0x976F47F2', '0x97E287D6', '0x98BD3B68', '0x9ADBFC13', '0x9ADD23AF', '0x9AF15027', '0x9D42800F', '0x9DA1A22E', '0x9E6B94A9', '0x9EA10E22', '0x9F43E0B8', '0x9F584A19', '0x9F92B239', '0xA008D384', '0xA0B0D059', '0xA171FA71', '0xA27F141D', '0xA2BDF63D', '0xA4421E17', '0xA48E8885', '0xA498EA47', '0xA4A34031', '0xA5D7810E', '0xA6133FA7', '0xA61DBACC', '0xA711AD5D', '0xA8D8998B', '0xAA16136E', '0xAAF04F48', '0xABC726AB', '0xAC6CEFC0', '0xAC88F06D', '0xACC8F105', '0xAD3C46A3', '0xAD98C754', '0xAE8E6F47', '0xB0302DF0', '0xB16C1E2F', '0xB171D55A', '0xB1AC743B', '0xB301105E', '0xB3476505', '0xB3D49A69', '0xB3FB1718', '0xB43703D3', '0xB4B34F05', '0xB4DAA22E', '0xB59E410D', '0xB5F24E61', '0xB6DFA41B', '0xB7980AA6', '0xB90198EE', '0xBABBF18F', '0xBAED2049', '0xBB35D2E9', '0xBBCC55A2', '0xBC5D1DE2', '0xBD4A5E9B', '0xBE11EA4F', '0xBE1AA31A', '0xBFE79BBB', '0xC04DF639', '0xC104641A', '0xC140C994', '0xC202EF7C', '0xC4B065EC', '0xC69379BD', '0xC8383803', '0xC842C91B', '0xC8EA68B8', '0xC9440E17', '0xC96E610A', '0xCA0C437D', '0xCA2F5A86', '0xCB17B892', '0xCCAC4C5B', '0xCD1EE842', '0xCD23590C', '0xCDA56980', '0xD1478B56', '0xD287A031', '0xD4B3B908', '0xD4FEA5E1', '0xD5DF3B68', '0xD60741EA', '0xD6206703', '0xD6429347', '0xD6ADFDC1', '0xD6C72D44', '0xD6E395BA', '0xD78BAEB0', '0xD7A09FA8', '0xD81DE630', '0xD8F5AF6E', '0xD9339F51', '0xDA2E8870', '0xDAE09A0F', '0xDAECAAE8', '0xDBEF78BF', '0xDC37D835', '0xDC67907B', '0xDC841529', '0xDDB93FB2', '0xDF331993', '0xE05E8AC8', '0xE0E0F586', '0xE0EBB383', '0xE199E192', '0xE230B836', '0xE24F2844', '0xE3E3BE2F', '0xE53BA58A', '0xE686D33C', '0xE6F05B35', '0xE7AAF665', '0xE80CB09B', '0xE977A7EF', '0xE9AEF248', '0xE9CBE5D9', '0xEA4ED7F8', '0xEA7256DE', '0xEB02613B', '0xEB132AD3', '0xEBF8C581', '0xEC8CF2D4', '0xEE1349F7', '0xEE6E6615', '0xEE9E4601', '0xEF407992', '0xF0C68BB6', '0xF2EA5A13', '0xF30866DD', '0xF3793395', '0xF37A3CCD', '0xF446FF01', '0xF483436A', '0xF78A6616', '0xF850B3A5', '0xF8F5D2C0', '0xF9BFA4F5', '0xF9FC4248', '0xFAB4DDE6', '0xFBA39348', '0xFDA06AA9', '0xFDB7A400', '0xFE619717', '0xFF0E4661']

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
    wdf = WDF.objects.get(name="photo.wdf")
    was_list = res_manager.get_wdf_file_list(wdf.name)
    print(was_list)
    return HttpResponse("success!")


def task(request):
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