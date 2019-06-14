from base.models.map import Map, get_version
from base.models.npc import NPC


def network_get_npc_list(self, data):
    """

    """
    _map = Map.objects.get(map_id=data['map_id'], version=get_version(data['map_version']))
    npc_models = NPC.objects.filter(map=_map)
    npc_list = []
    for npc in npc_models:
        if npc.npc_type == 1:  # 传送NPC
            npc_list.append({
                'npc_name': npc.name,
                'npc_id': npc.id,
                'npc_type': 1,
                'res_info': {'normal': [npc.res.was.wdf.name, npc.res.was.hash]},
                'direction': npc.direction,
                'map_id': npc.map.map_id,
                'map_version': npc.map.version,
                'x': npc.x,
                'y': npc.y})
    send_data = {
        'action': "receive_npc_list",
        'map_id': data['map_id'],
        'map_version': data['map_version'],
        'npc_list': npc_list
    }
    print(send_data)
    self.transmit(send_data)
