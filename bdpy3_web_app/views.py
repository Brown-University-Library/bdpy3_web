# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint

from bdpy3_web_app import settings_app
from bdpy3_web_app.lib import version_helper
from bdpy3_web_app.lib.app_helper import Validator, LibCaller
from bdpy3_web_app.lib.lib_caller import V2RequestBibCaller
from bdpy3_web_app.lib.validator import V2RequestValidator
from django.conf import settings
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseNotFound
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
    log.debug( '\n\n\nstarting exact-request...' )
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
    log.debug( '\n\n\nstarting bib-request...' )
    if v2_request_validator.validate_bib_request( request.method, request.META.get('REMOTE_ADDR', ''), request.POST ) is False:
        log.info( 'request invalid, returning 400' )
        return HttpResponseBadRequest( '400 / Bad Request' )
    ( patron_barcode, title, author, year ) = ( request.POST['patron_barcode'], request.POST['title'], request.POST['author'], request.POST['year'] )
    result_dct = v2_request_bib_caller.request_bib( patron_barcode, title, author, year )
    log.debug( 'returning response' )
    jsn = json.dumps( result_dct, sort_keys=True, indent=2 )
    return HttpResponse( jsn, content_type='application/javascript; charset=utf-8' )


def access_test( request ):
    """ Returns simplest response. """
    log.debug( f'\n\n\nstarting access_test; request, ```{request.__dict__}```' )
    now = datetime.datetime.now()
    return HttpResponse( '<p>hi</p> <p>( %s )</p>' % now )


# ===========================
# for development convenience
# ===========================


def version( request ):
    """ Returns basic branch and commit data. """
    rq_now = datetime.datetime.now()
    commit = version_helper.get_commit()
    branch = version_helper.get_branch()
    info_txt = commit.replace( 'commit', branch )
    context = version_helper.make_context( request, rq_now, info_txt )
    output = json.dumps( context, sort_keys=True, indent=2 )
    return HttpResponse( output, content_type='application/json; charset=utf-8' )


def error_check( request ):
    """ For checking that admins receive error-emails. """
    if settings.DEBUG == True:
        1/0
    else:
        return HttpResponseNotFound( '<div>404 / Not Found</div>' )
