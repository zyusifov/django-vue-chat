## Minimal chat web application on vue/django

*In this project i'm use:*
- Vue.js
- Django
- Django Channels
- Redis

### For start
`daphne config.asgi:application` - backend
`docker run --name django-vue-chat -p 6379:6379 -d redis` - redis
