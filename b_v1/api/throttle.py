from rest_framework.throttling import UserRateThrottle


class PostViewThrottle(UserRateThrottle):
    scope = 'blog-list'


class PostDetailThrottle(UserRateThrottle):
    scope = 'post-detail'
