""" Transform """

from __future__ import absolute_import
from eea.privacyscreen.base import ATTRIBUTES
from eea.privacyscreen.base import get_domain
from plone.outputfilters.interfaces import IFilter
from zope.interface import implementer

import lxml.html


try:
    from urllib.parse import urlencode
except ImportError:
    import six.moves.urllib.request
    import six.moves.urllib.parse
    import six.moves.urllib.error
    urlencode = six.moves.urllib.parse.urlencode


@implementer(IFilter)
class IframeFilter(object):
    """ Filter """
    order = 0

    def __init__(self, context, request):
        pass

    def is_enabled(self):
        """ Enable """

        return True

    def process(self, node):
        """ Process """

        # import pdb
        # pdb.set_trace()
        src = node.get('src')

        # data-embed-group (group)
        # data-embed-screenshot (screenshot)
        # data-embed-title (embed_title)

        domain = get_domain(src)
        if not domain:
            return False

        data = {}
        for k, v in ATTRIBUTES.items():
            a = node.get(k)
            if a:
                data[v] = a

        data['group'] = domain or data.get('group')
        data['src'] = src

        qs = urlencode(data)

        src = './@@embed?' + qs

        node.set('src', src)

        return True

    def __call__(self, data):
        etree = lxml.html.fromstring(data)
        iframes = etree.xpath('//iframe')

        changed = [self.process(node) for node in iframes]
        if any(changed):
            data = lxml.html.tostring(etree)

        return data
