import json

from aiohttp import web

import auto_db
import exceptions


async def index(request) -> web.Response:
    """
    An index page
    :param request:
    :return:
    """
    response_object = {
        'status': 'success'
    }

    return web.Response(text=json.dumps(response_object), status=200, content_type='application/json')


async def get_auto(request) -> web.Response:
    """
    Allows to get autos list and filter them
    :param request:
    :return:
    """

    response_object = {
        'status': 'success',
        'data': auto_db.get_all(request.query)
    }

    return web.Response(text=json.dumps(response_object), status=200, content_type='application/json')


async def create_auto(request) -> web.Response:
    response_object = {
        'status': 'success',
        'data': auto_db.create_new(request.query)
    }

    return web.Response(text=json.dumps(response_object), status=200, content_type='application/json')


async def view_auto(request) -> web.Response:
    try:
        response_object = {
            'status': 'success',
            'data': auto_db.get_one(request.query['id'])
        }

        return web.Response(text=json.dumps(response_object), status=200, content_type='application/json')

    except KeyError as e:
        response_object = {
            'status': 'error',
            'message': 'Specify {} param'.format(str(e)),
        }

        return web.Response(text=json.dumps(response_object), status=500, content_type='application/json')

    except exceptions.NotFound as e:
        response_object = {
            'status': 'error',
            'message': str(e),
        }

        return web.Response(text=json.dumps(response_object), status=404, content_type='application/json')


async def update_auto(request) -> web.Response:
    try:
        response_object = {
            'status': 'success',
            'data': auto_db.update(request.query)
        }

        return web.Response(text=json.dumps(response_object), status=200, content_type='application/json')

    except KeyError as e:
        response_object = {
            'status': 'error',
            'message': 'Specify {} param'.format(str(e)),
        }

        return web.Response(text=json.dumps(response_object), status=500, content_type='application/json')

    except exceptions.NotFound as e:
        response_object = {
            'status': 'error',
            'message': str(e),
        }

        return web.Response(text=json.dumps(response_object), status=404, content_type='application/json')


async def delete_auto(request) -> web.Response:
    try:
        auto_db.delete(request.query['id'])

        response_object = {
            'status': 'success',
        }

        return web.Response(text=json.dumps(response_object), status=200, content_type='application/json')

    except KeyError as e:
        response_object = {
            'status': 'error',
            'message': 'Specify {} param'.format(str(e)),
        }

        return web.Response(text=json.dumps(response_object), status=500, content_type='application/json')

    except exceptions.NotFound as e:
        response_object = {
            'status': 'error',
            'message': str(e),
        }

        return web.Response(text=json.dumps(response_object), status=404, content_type='application/json')


if __name__ == '__main__':
    app = web.Application()

    # Set routes
    app.router.add_get('/', index)
    app.router.add_get('/auto', get_auto)
    app.router.add_get('/auto/view', view_auto)
    app.router.add_put('/auto/create', create_auto)
    app.router.add_post('/auto/update', update_auto)
    app.router.add_delete('/auto/delete', delete_auto)

    web.run_app(app)
