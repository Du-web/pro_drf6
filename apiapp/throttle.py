from rest_framework.throttling import ScopedRateThrottle


class MyThrottle(ScopedRateThrottle):
    scope = 'my'

    def get_cache_key(self, request, view):
        phone = request.query_params.get('phone')
        if not phone:
            return None
        return 'throttle_%(scope)s_%(ident)s' % {'scope': self.scope, 'ident': phone}