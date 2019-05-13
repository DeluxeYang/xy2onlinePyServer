from base.models.map import Map
from base.models.portal import Portal


def network_get_portal_list(self, data):
    """
    获取角色全部信息
    必要参数：character_id
    """
    portal_models = Portal.objects.filter(map__map_id=data['map_id'])
    portal_list = [{
        'type': 'portal',
        'map_id': data['map_id'],
        'x': portal.x,
        'y': portal.y,
        'res_info': {'normal': [portal.res.was.wdf.name, portal.res.was.hash]},
        'target_map_version': portal.target_map.version_choice[portal.target_map.version][1],
        'target_map_id': portal.target_map.map_id,
        'target_x': portal.target_x,
        'target_y': portal.target_y}
        for portal in portal_models]
    send_data = {
        'action': "receive_portal_list",
        'map_id': data['map_id'],
        'portal_list': portal_list
    }
    print(send_data)
    self.transmit(send_data)
