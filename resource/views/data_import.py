from django.shortcuts import HttpResponse
from resource.utils.ResManager import res_manager
from resource.models.wdf import WDF, WAS
from resource.models.character import *
# Create your views here.

from .data.characters_data import characters


def wdf_import(request):
    wdf = WDF.objects.get(name="shape.wdf")
    was_list = []
    count = 0
    for _hash in was_list:
        was = WAS()
        was.wdf = wdf
        was.hash = _hash
        flag = was.save()
        if flag:
            count += 1
    return HttpResponse(str(len(was_list)) + "success!" + str(count))


def get_was_list(request):
    wdf = WDF.objects.get(name="shape.wdf")
    was_list = res_manager.get_wdf_file_list(wdf.name)
    print(was_list)
    return HttpResponse("success!")


def character_import(request):
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