from django.shortcuts import HttpResponse
from resource.utils.ResManager import res_manager
from resource.models.wdf import WDF, WAS
from resource.models.character import *
# Create your views here.

from .data.characters_data import characters


def character_import(request):
    for race_name in characters:
        for character_name in characters[race_name]:
            character_info = characters[race_name][character_name]

            race = Race.objects.get(name=race_name)
            new_character = Character()
            new_character.race = race
            new_character.name = character_name
            new_character.name_cn = character_info["name"]
            new_character.gender = -1 if character_info["gender"] == 0 else 1
            new_character.describe = character_info["describe"]
            new_character.save()
            for action_name in ["run", "stand", "stand_tease", "walk"]:

                new_action = CharacterAction()
                new_action.character = new_character
                new_action.name = action_name

                action = character_info[action_name]

                wdf = WDF.objects.get(name=action[0])
                was = WAS()
                was.wdf = wdf
                was.hash = action[1]
                was.hooked = True
                was.describe = character_name + ": " + action_name
                was.save()

                new_action.was = was
                new_action.save()

            for weapon_name in character_info["weapon"]:
                for action_name in character_info["weapon"][weapon_name]:
                    new_action = CharacterAction()
                    new_action.character = new_character
                    new_action.name = action_name
                    new_action.weapon = weapon_name

                    action = character_info["weapon"][weapon_name][action_name]

                    wdf = WDF.objects.get(name=action[0])
                    was = WAS()
                    was.wdf = wdf
                    was.hash = action[1]
                    was.hooked = True
                    was.describe = character_name + ": " + action_name
                    was.save()

                    new_action.was = was
                    new_action.save()

    return HttpResponse("success!")

def wdf_import(request):
    wdf = WDF.objects.get(name="shape.wdf")
    was_list = ['0xC0C44A3E', '0xC1B24BAC', '0xC1B738F2', '0xC1BE763B', '0xC1C6F80B', '0xC1C99339', '0xC21EE597', '0xC230BE81', '0xC27E40BA', '0xC2A778B1', '0xC2B4BFF3', '0xC2D2E710', '0xC3578B7F', '0xC378B04A', '0xC3C3CE08', '0xC3C9319C', '0xC41FEF07', '0xC463B972', '0xC48290AA', '0xC4B8903E', '0xC5676415', '0xC56DDF51', '0xC5A63D43', '0xC5C3FCC4', '0xC5CF4D09', '0xC631BB84', '0xC6808FEC', '0xC6D7CC10', '0xC6EC792F', '0xC6F66D15', '0xC742FDEF', '0xC748867C', '0xC756DE61', '0xC7766014', '0xC79B407C', '0xC7EAC3F1', '0xC7F51159', '0xC82770E2', '0xC8406125', '0xC87B8D00', '0xC888F0C3', '0xC8B56AAB', '0xC8E3CA0D', '0xC92F7E24', '0xC944B9F3', '0xC988FB25', '0xC9EC64BB', '0xCA26616D', '0xCA3334FF', '0xCA5F4A5F', '0xCAAB76D5', '0xCAB2E6BF', '0xCAB5EFEB', '0xCACD3019', '0xCAFDA26D', '0xCB14A5E2', '0xCB48E23B', '0xCB62E343', '0xCC61903E', '0xCC9CE563', '0xCCCED404', '0xCCDAD36E', '0xCD3B5103', '0xCD9D7671', '0xCDA62DBA', '0xCDEE504D', '0xCE262DF2', '0xCE391F52', '0xCE62A786', '0xCE7F6140', '0xCEAF6543', '0xCEF45818', '0xCF4C2B84', '0xCF8E36F8', '0xCFCC8F6F', '0xCFE04A15', '0xD01C7435', '0xD02A9BB5', '0xD0829F8F', '0xD08E3166', '0xD0C2CA2D', '0xD0C5FFC8', '0xD10CC290', '0xD117595B', '0xD123DBD0', '0xD12EB5E3', '0xD1518AFF', '0xD163F10A', '0xD1939D57', '0xD1C83AD0', '0xD1CE3228', '0xD1E67B5B', '0xD21DE04A', '0xD25E9FF0', '0xD29E8F5D', '0xD2E4149E', '0xD2EBBC01', '0xD317B92D', '0xD3B754A3', '0xD4265BBB', '0xD42B054A', '0xD463B910', '0xD4B0D0B3', '0xD4B50A16', '0xD4B8C139', '0xD4D2D232', '0xD4F344C4', '0xD50ED0F4', '0xD5332E6D', '0xD55B8806', '0xD572D8E4', '0xD5D3DBA9', '0xD67C2CB8', '0xD69D74DA', '0xD6AFCAC2', '0xD6C941FC', '0xD6CD4B82', '0xD6F382BA', '0xD70C8074', '0xD719314F', '0xD72C8A4B', '0xD73020CD', '0xD7505720', '0xD7A74DE2', '0xD7B9E45C', '0xD7DC93DE', '0xD817F82F', '0xD86A15E2', '0xD8E9B5FE', '0xD93306AD', '0xD9366D7C', '0xD945737B', '0xD954D814', '0xD97E30F0', '0xD9A42849', '0xD9C108BF', '0xDA002F0B', '0xDA0F8408', '0xDA498AD2', '0xDA4C1796', '0xDAC84F94', '0xDAFF18F4', '0xDB11C815', '0xDB1716B1', '0xDB189AC5', '0xDB4600C4', '0xDB68BB03', '0xDBA9BE37', '0xDC2C33F6', '0xDC606593', '0xDCF6A150', '0xDD0B0D7A', '0xDD102EC4', '0xDD1F37DE', '0xDD52C93A', '0xDD757619', '0xDD820CF0', '0xDD86B4EC', '0xDD9132B6', '0xDDF4FEC5', '0xDE2A0E4A', '0xDE318B4E', '0xDE58CA6F', '0xDE5A0BC6', '0xDE7DA687', '0xDE984023', '0xDEA8818C', '0xDEBBC85B', '0xDEC9CC5B', '0xDECD5B16', '0xDECDF4A2', '0xDF976C1E', '0xDFAB4445', '0xDFB3D729', '0xDFBB7D6C', '0xE01F9B56', '0xE05ACDC6', '0xE06B51C5', '0xE08BBB1A', '0xE0DC6D93', '0xE0F602EC', '0xE10904E5', '0xE10AB87A', '0xE1380841', '0xE17C5C52', '0xE1A120FF', '0xE1BFCF0D', '0xE1D303C3', '0xE1E4E409', '0xE1E89EB6', '0xE202FF07', '0xE2066294', '0xE21F96D1', '0xE265FD65', '0xE26DD56F', '0xE2979F4F', '0xE2DD30D1', '0xE2F32AF1', '0xE325DA76', '0xE3587E7B', '0xE37D1868', '0xE382FDA7', '0xE383DE59', '0xE3E15EAC', '0xE4042BBF', '0xE425B3FE', '0xE432C378', '0xE436F2B8', '0xE44571AA', '0xE490BFA3', '0xE4926FC7', '0xE4FD5CC5', '0xE513139F', '0xE53AB100', '0xE567D488', '0xE59A8113', '0xE6914BD4', '0xE6ABAE51', '0xE6AD8241', '0xE6E5F66E', '0xE6E7DE44', '0xE6F0D923', '0xE74D58A9', '0xE759FD0F', '0xE78B25C1', '0xE7CF4AE4', '0xE8104475', '0xE8A7D963', '0xE8B26ECF', '0xE8C2C0A4', '0xE91E294B', '0xE94B69B0', '0xE97AC333', '0xE985EE5D', '0xE9AD975F', '0xEA27AD31', '0xEA36DB67', '0xEAB43B8D', '0xEB00DE5F', '0xEB0F0E80', '0xEB15762A', '0xEB5088EA', '0xEB8235CF', '0xEB9300D7', '0xEBE564E7', '0xEC3FC0DC', '0xEC66721B', '0xEC6F79F4', '0xEC91EDA2', '0xECB28752', '0xECBF1A3D', '0xED6DCE25', '0xED788B3D', '0xED850381', '0xEDBC3127', '0xEDC7FB4A', '0xEE809210', '0xEE9F2B14', '0xEF445F94', '0xEF49D689', '0xEF4D4EBB', '0xEF57B6C6', '0xEFC69175', '0xF09E9903', '0xF0ACEB35', '0xF10437EF', '0xF113D230', '0xF16C471C', '0xF1AA55F6', '0xF1E86993', '0xF20F8357', '0xF22082F6', '0xF225F2D5', '0xF250443E', '0xF26D871D', '0xF32E07A3', '0xF33532BD', '0xF34E1359', '0xF37623A9', '0xF3EA33B1', '0xF3F3CA4F', '0xF3FD7A0F', '0xF41F6038', '0xF43E4F12', '0xF4411DFD', '0xF44C3FDE', '0xF4588069', '0xF45ED5CE', '0xF4848781', '0xF49E974E', '0xF4B285BA', '0xF4DAD89F', '0xF4FE5557', '0xF516BD4A', '0xF577111E', '0xF57D6266', '0xF58104E2', '0xF58E06E8', '0xF59C9968', '0xF5B913D8', '0xF5D47E2E', '0xF6210AA0', '0xF637E75A', '0xF63FDBF2', '0xF6739CAE', '0xF69A1184', '0xF7001687', '0xF704761A', '0xF707EA37', '0xF70BAA25', '0xF735C9A9', '0xF7545337', '0xF7937617', '0xF7A903E3', '0xF846C711', '0xF879501E', '0xF87D8A2A', '0xF8A2C37A', '0xF8C16862', '0xF9321464', '0xF98BEFBD', '0xF9B292E5', '0xF9B81AB9', '0xF9E47CD2', '0xF9F2A3F2', '0xFA3CAFE4', '0xFA5EB5FF', '0xFA74CEC4', '0xFAA9511F', '0xFAADCE7F', '0xFB015381', '0xFB352928', '0xFB40C501', '0xFB629346', '0xFB6C8326', '0xFBAECC68', '0xFBB719F3', '0xFBB7A2A2', '0xFBC04019', '0xFC1AD8BE', '0xFC527CFF', '0xFC590C8D', '0xFC70AC0B', '0xFD266883', '0xFD419E2C', '0xFD78B79C', '0xFD851096', '0xFDE88236', '0xFEC040B1', '0xFED46831', '0xFF037975', '0xFF1F0166', '0xFF25D8BA', '0xFF27CA9E', '0xFF5A4EAA', '0xFF6D3B35', '0xFF76393B', '0xFF7FBE19', '0xFF851D2E', '0xFFD5F67A']
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
