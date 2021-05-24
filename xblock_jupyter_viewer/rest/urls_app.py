from django.apps import AppConfig


""" 
    I DO NOT BELIEVE THIS IS IN USE AT ALL, 
    these urls were manually added to the 
    hydrolearn/edx-platform repo under the branch
    "hydrolearn/koa.3-master"

 """

# edx plugin to map urls for jupiter viewer xblock
class JupyterViewerURLPluginApp(AppConfig):
    # needs an actual full path
    name = 'xblock_jupyter_viewer.rest'

    plugin_app = {
        'url_config': {
            'lms.djangoapp':{
                'namespace' : 'xblock_jupyter_viewer',
                'relative_path': 'urls',
                'regex': '^api/jupyter/',
            },
            'cms.djangoapp':{
                'namespace' : 'xblock_jupyter_viewer',
                'relative_path': 'urls',
                'regex': '^api/jupyter/',
            }

        }
    }