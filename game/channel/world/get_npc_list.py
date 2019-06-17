from base.models.map import Map, get_version
from base.models.npc import NPC
from resource.models.shape import ShapeAction
from base.models.npc_target import NPCTarget


def network_get_npc_list(self, data):
    """

    """
    _map = Map.objects.get(map_id=data['map_id'], version=get_version(data['map_version']))
    npc_models = NPC.objects.filter(map=_map)
    npc_list = []
    for npc in npc_models:
        if npc.npc_type == 1:  # 传送NPC
            npc_data = {
                'type': "npc",
                'npc_name': npc.name,
                'npc_id': npc.id,
                'npc_type': 1,
                'res_info': {},
                'direction': npc.direction,
                'map_id': npc.map.map_id,
                'map_version': npc.map.version,
                'x': npc.x,
                'y': npc.y,
                'addition': []
            }
            shape_actions = ShapeAction.objects.filter(shape=npc.res)
            for action in shape_actions:
                npc_data["res_info"][action.name] = [action.was.wdf.name, action.was.hash]
            target_models = NPCTarget.objects.filter(npc=npc)
            for target in target_models:
                npc_data["addition"].append({
                    "target_map_id": target.target_map.map_id,
                    'target_map_version': target.target_map.version_choice[target.target_map.version][1],
                    'target_x': target.target_x,
                    'target_y': target.target_y})
            npc_list.append(npc_data)
    send_data = {
        'action': "receive_npc_list",
        'map_id': data['map_id'],
        'map_version': data['map_version'],
        'npc_list': npc_list
    }
    print(send_data)
    self.transmit(send_data)
