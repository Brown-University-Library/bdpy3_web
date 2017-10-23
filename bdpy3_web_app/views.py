# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint
from bdpy3_web_app import settings_app
from bdpy3_web_app.lib.app_helper import Validator, LibCaller
from bdpy3_web_app.lib.lib_caller import V2RequestBibCaller
from bdpy3_web_app.lib.validator import V2RequestValidator
from django.conf import settings
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


log = logging.getLogger(__name__)

caller = LibCaller()
v1_validator = Validator()
v2_request_bib_caller = V2RequestBibCaller()
v2_request_validator = V2RequestValidator()


def info( request ):
    """ Returns simplest response. """
    return HttpResponseRedirect( settings_app.README_URL )


def v1( request ):
    """ Handles v1 request-exact post from easyborrow & returns json results. """
    # log.debug( 'request, ```%s```' % pprint.pformat(request.__dict__) )
    log.debug( '\n\nstarting request...' )
    if v1_validator.validate_request( request.method, request.META.get('REMOTE_ADDR', ''), request.POST ) is False:
        log.info( 'request invalid, returning 400' )
        return HttpResponseBadRequest( '400 / Bad Request' )
    result_data = caller.request_exact( request.POST )
    interpreted_response_dct = caller.interpret_result( result_data )
    log.debug( 'returning response' )
    jsn = json.dumps( interpreted_response_dct, sort_keys=True, indent=2 )
    return HttpResponse( jsn, content_type='application/javascript; charset=utf-8' )


def v2_bib_request( request ):
    """ Handles v1 request-exact post from easyborrow & returns json results. """
    log.debug( '\n\nstarting bib-request...' )
    if v2_request_validator.validate_bib_request( request.method, request.META.get('REMOTE_ADDR', ''), request.POST ) is False:
        log.info( 'request invalid, returning 400' )
        return HttpResponseBadRequest( '400 / Bad Request' )
    result_data = v2_request_bib_caller.request_bib( request.POST )
    response_dct = v2_request_bib_caller.make_response( result_data )
    log.debug( 'returning response' )
    jsn = json.dumps( interpreted_response_dct, sort_keys=True, indent=2 )
    return HttpResponse( jsn, content_type='application/javascript; charset=utf-8' )


def access_test( request ):
    """ Returns simplest response. """
    log.debug( 'request, ```%s```' % pprint.pformat(request.__dict__) )
    now = datetime.datetime.now()
    return HttpResponse( '<p>hi</p> <p>( %s )</p>' % now )
