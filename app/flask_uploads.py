# -*- coding: utf-8 -*-
"""
flaskext.uploads
================
This module provides upload support for Flask. The basic pattern is to set up
an `UploadSet` object and upload your files to it.
<<<<<<< HEAD
:copyright: 2010 Matthew "LeafStorm" Frazier
:license:   MIT/X11, see LICENSE for details
"""
import sys
PY3 = sys.version_info[0] == 3
=======

:copyright: 2010 Matthew "LeafStorm" Frazier
:license:   MIT/X11, see LICENSE for details
"""

import sys

PY3 = sys.version_info[0] == 3

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
if PY3:
    string_types = str,
else:
    string_types = basestring,
<<<<<<< HEAD
import os.path
import posixpath
=======

import os.path
import posixpath

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
from flask import current_app, send_from_directory, abort, url_for
from itertools import chain
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
<<<<<<< HEAD
from flask import Blueprint
# Extension presets
#: This just contains plain text files (.txt).
TEXT = ('txt',)
=======

from flask import Blueprint

# Extension presets

#: This just contains plain text files (.txt).
TEXT = ('txt',)

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
#: This contains various office document formats (.rtf, .odf, .ods, .gnumeric,
#: .abw, .doc, .docx, .xls, and .xlsx). Note that the macro-enabled versions
#: of Microsoft Office 2007 files are not included.
DOCUMENTS = tuple('rtf odf ods gnumeric abw doc docx xls xlsx'.split())
<<<<<<< HEAD
#: This contains basic image types that are viewable from most browsers (.jpg,
#: .jpe, .jpeg, .png, .gif, .svg, and .bmp).
IMAGES = tuple('jpg jpe jpeg png gif svg bmp'.split())
#: This contains audio file types (.wav, .mp3, .aac, .ogg, .oga, and .flac).
AUDIO = tuple('wav mp3 aac ogg oga flac'.split())
#: This is for structured data files (.csv, .ini, .json, .plist, .xml, .yaml,
#: and .yml).
DATA = tuple('csv ini json plist xml yaml yml'.split())
=======

#: This contains basic image types that are viewable from most browsers (.jpg,
#: .jpe, .jpeg, .png, .gif, .svg, and .bmp).
IMAGES = tuple('jpg jpe jpeg png gif svg bmp'.split())

#: This contains audio file types (.wav, .mp3, .aac, .ogg, .oga, and .flac).
AUDIO = tuple('wav mp3 aac ogg oga flac'.split())

#: This is for structured data files (.csv, .ini, .json, .plist, .xml, .yaml,
#: and .yml).
DATA = tuple('csv ini json plist xml yaml yml'.split())

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
#: This contains various types of scripts (.js, .php, .pl, .py .rb, and .sh).
#: If your Web server has PHP installed and set to auto-run, you might want to
#: add ``php`` to the DENY setting.
SCRIPTS = tuple('js php pl py rb sh'.split())
<<<<<<< HEAD
#: This contains archive and compression formats (.gz, .bz2, .zip, .tar,
#: .tgz, .txz, and .7z).
ARCHIVES = tuple('gz bz2 zip tar tgz txz 7z'.split())
=======

#: This contains archive and compression formats (.gz, .bz2, .zip, .tar,
#: .tgz, .txz, and .7z).
ARCHIVES = tuple('gz bz2 zip tar tgz txz 7z'.split())

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
#: This contains shared libraries and executable files (.so, .exe and .dll).
#: Most of the time, you will not want to allow this - it's better suited for
#: use with `AllExcept`.
EXECUTABLES = tuple('so exe dll'.split())
<<<<<<< HEAD
#: The default allowed extensions - `TEXT`, `DOCUMENTS`, `DATA`, and `IMAGES`.
DEFAULTS = TEXT + DOCUMENTS + IMAGES + DATA
=======

#: The default allowed extensions - `TEXT`, `DOCUMENTS`, `DATA`, and `IMAGES`.
DEFAULTS = TEXT + DOCUMENTS + IMAGES + DATA


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
class UploadNotAllowed(Exception):
    """
    This exception is raised if the upload was not allowed. You should catch
    it in your view code and display an appropriate message to the user.
    """
<<<<<<< HEAD
def tuple_from(*iters):
    return tuple(itertools.chain(*iters))
=======


def tuple_from(*iters):
    return tuple(itertools.chain(*iters))


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
def extension(filename):
    ext = os.path.splitext(filename)[1]
    if ext.startswith('.'):
        # os.path.splitext retains . separator
        ext = ext[1:]
    return ext
<<<<<<< HEAD
=======


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
def lowercase_ext(filename):
    """
    This is a helper used by UploadSet.save to provide lowercase extensions for
    all processed files, to compare with configured extensions in the same
    case.
<<<<<<< HEAD
    .. versionchanged:: 0.1.4
       Filenames without extensions are no longer lowercased, only the
       extension is returned in lowercase, if an extension exists.
=======

    .. versionchanged:: 0.1.4
       Filenames without extensions are no longer lowercased, only the
       extension is returned in lowercase, if an extension exists.

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    :param filename: The filename to ensure has a lowercase extension.
    """
    if '.' in filename:
        main, ext = os.path.splitext(filename)
        return main + ext.lower()
    # For consistency with os.path.splitext,
    # do not treat a filename without an extension as an extension.
    # That is, do not return filename.lower().
    return filename
<<<<<<< HEAD
=======


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
def addslash(url):
    if url.endswith('/'):
        return url
    return url + '/'
<<<<<<< HEAD
=======


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
def patch_request_class(app, size=64 * 1024 * 1024):
    """
    By default, Flask will accept uploads to an arbitrary size. While Werkzeug
    switches uploads from memory to a temporary file when they hit 500 KiB,
    it's still possible for someone to overload your disk space with a
    gigantic file.
<<<<<<< HEAD
    This patches the app's request class's
    `~werkzeug.BaseRequest.max_content_length` attribute so that any upload
    larger than the given size is rejected with an HTTP error.
    .. note::
=======

    This patches the app's request class's
    `~werkzeug.BaseRequest.max_content_length` attribute so that any upload
    larger than the given size is rejected with an HTTP error.

    .. note::

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
       In Flask 0.6, you can do this by setting the `MAX_CONTENT_LENGTH`
       setting, without patching the request class. To emulate this behavior,
       you can pass `None` as the size (you must pass it explicitly). That is
       the best way to call this function, as it won't break the Flask 0.6
       functionality if it exists.
<<<<<<< HEAD
    .. versionchanged:: 0.1.1
=======

    .. versionchanged:: 0.1.1

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    :param app: The app to patch the request class of.
    :param size: The maximum size to accept, in bytes. The default is 64 MiB.
                 If it is `None`, the app's `MAX_CONTENT_LENGTH` configuration
                 setting will be used to patch.
    """
    if size is None:
        if isinstance(app.request_class.__dict__['max_content_length'],
                      property):
            return
        size = app.config.get('MAX_CONTENT_LENGTH')
    reqclass = app.request_class
    patched = type(reqclass.__name__, (reqclass,),
                   {'max_content_length': size})
    app.request_class = patched
<<<<<<< HEAD
=======


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
def config_for_set(uset, app, defaults=None):
    """
    This is a helper function for `configure_uploads` that extracts the
    configuration for a single set.
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    :param uset: The upload set.
    :param app: The app to load the configuration from.
    :param defaults: A dict with keys `url` and `dest` from the
                     `UPLOADS_DEFAULT_DEST` and `DEFAULT_UPLOADS_URL`
                     settings.
    """
    config = app.config
    prefix = 'UPLOADED_%s_' % uset.name.upper()
    using_defaults = False
    if defaults is None:
        defaults = dict(dest=None, url=None)
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    allow_extns = tuple(config.get(prefix + 'ALLOW', ()))
    deny_extns = tuple(config.get(prefix + 'DENY', ()))
    destination = config.get(prefix + 'DEST')
    base_url = config.get(prefix + 'URL')
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    if destination is None:
        # the upload set's destination wasn't given
        if uset.default_dest:
            # use the "default_dest" callable
            destination = uset.default_dest(app)
        if destination is None: # still
            # use the default dest from the config
            if defaults['dest'] is not None:
                using_defaults = True
                destination = os.path.join(defaults['dest'], uset.name)
            else:
                raise RuntimeError("no destination for set %s" % uset.name)
<<<<<<< HEAD
    if base_url is None and using_defaults and defaults['url']:
        base_url = addslash(defaults['url']) + uset.name + '/'
    return UploadConfiguration(destination, base_url, allow_extns, deny_extns)
=======

    if base_url is None and using_defaults and defaults['url']:
        base_url = addslash(defaults['url']) + uset.name + '/'

    return UploadConfiguration(destination, base_url, allow_extns, deny_extns)


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
def configure_uploads(app, upload_sets):
    """
    Call this after the app has been configured. It will go through all the
    upload sets, get their configuration, and store the configuration on the
    app. It will also register the uploads module if it hasn't been set. This
    can be called multiple times with different upload sets.
<<<<<<< HEAD
    .. versionchanged:: 0.1.3
       The uploads module/blueprint will only be registered if it is needed
       to serve the upload sets.
=======

    .. versionchanged:: 0.1.3
       The uploads module/blueprint will only be registered if it is needed
       to serve the upload sets.

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    :param app: The `~flask.Flask` instance to get the configuration from.
    :param upload_sets: The `UploadSet` instances to configure.
    """
    if isinstance(upload_sets, UploadSet):
        upload_sets = (upload_sets,)
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    if not hasattr(app, 'upload_set_config'):
        app.upload_set_config = {}
    set_config = app.upload_set_config
    defaults = dict(dest=app.config.get('UPLOADS_DEFAULT_DEST'),
                    url=app.config.get('UPLOADS_DEFAULT_URL'))
<<<<<<< HEAD
    for uset in upload_sets:
        config = config_for_set(uset, app, defaults)
        set_config[uset.name] = config
    should_serve = any(s.base_url is None for s in set_config.values())
    if '_uploads' not in app.blueprints and should_serve:
        app.register_blueprint(uploads_mod)
=======

    for uset in upload_sets:
        config = config_for_set(uset, app, defaults)
        set_config[uset.name] = config

    should_serve = any(s.base_url is None for s in set_config.values())
    if '_uploads' not in app.blueprints and should_serve:
        app.register_blueprint(uploads_mod)


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
class All(object):
    """
    This type can be used to allow all extensions. There is a predefined
    instance named `ALL`.
    """
    def __contains__(self, item):
        return True
<<<<<<< HEAD
#: This "contains" all items. You can use it to allow all extensions to be
#: uploaded.
ALL = All()
=======


#: This "contains" all items. You can use it to allow all extensions to be
#: uploaded.
ALL = All()


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
class AllExcept(object):
    """
    This can be used to allow all file types except certain ones. For example,
    to ban .exe and .iso files, pass::
<<<<<<< HEAD
        AllExcept(('exe', 'iso'))
    to the `UploadSet` constructor as `extensions`. You can use any container,
    for example::
=======

        AllExcept(('exe', 'iso'))

    to the `UploadSet` constructor as `extensions`. You can use any container,
    for example::

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
        AllExcept(SCRIPTS + EXECUTABLES)
    """
    def __init__(self, items):
        self.items = items
<<<<<<< HEAD
    def __contains__(self, item):
        return item not in self.items
=======

    def __contains__(self, item):
        return item not in self.items


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
class UploadConfiguration(object):
    """
    This holds the configuration for a single `UploadSet`. The constructor's
    arguments are also the attributes.
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    :param destination: The directory to save files to.
    :param base_url: The URL (ending with a /) that files can be downloaded
                     from. If this is `None`, Flask-Uploads will serve the
                     files itself.
    :param allow: A list of extensions to allow, even if they're not in the
                  `UploadSet` extensions list.
    :param deny: A list of extensions to deny, even if they are in the
                 `UploadSet` extensions list.
    """
    def __init__(self, destination, base_url=None, allow=(), deny=()):
        self.destination = destination
        self.base_url = base_url
        self.allow = allow
        self.deny = deny
<<<<<<< HEAD
    @property
    def tuple(self):
        return (self.destination, self.base_url, self.allow, self.deny)
    def __eq__(self, other):
        return self.tuple == other.tuple
=======

    @property
    def tuple(self):
        return (self.destination, self.base_url, self.allow, self.deny)

    def __eq__(self, other):
        return self.tuple == other.tuple


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
class UploadSet(object):
    """
    This represents a single set of uploaded files. Each upload set is
    independent of the others. This can be reused across multiple application
    instances, as all configuration is stored on the application object itself
    and found with `flask.current_app`.
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    :param name: The name of this upload set. It defaults to ``files``, but
                 you can pick any alphanumeric name you want. (For simplicity,
                 it's best to use a plural noun.)
    :param extensions: The extensions to allow uploading in this set. The
                       easiest way to do this is to add together the extension
                       presets (for example, ``TEXT + DOCUMENTS + IMAGES``).
                       It can be overridden by the configuration with the
                       `UPLOADED_X_ALLOW` and `UPLOADED_X_DENY` configuration
                       parameters. The default is `DEFAULTS`.
    :param default_dest: If given, this should be a callable. If you call it
                         with the app, it should return the default upload
                         destination path for that app.
    """
    def __init__(self, name='files', extensions=DEFAULTS, default_dest=None):
        if not name.isalnum():
            raise ValueError("Name must be alphanumeric (no underscores)")
        self.name = name
        self.extensions = extensions
        self._config = None
        self.default_dest = default_dest
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    @property
    def config(self):
        """
        This gets the current configuration. By default, it looks up the
        current application and gets the configuration from there. But if you
        don't want to go to the full effort of setting an application, or it's
        otherwise outside of a request context, set the `_config` attribute to
        an `UploadConfiguration` instance, then set it back to `None` when
        you're done.
        """
        if self._config is not None:
            return self._config
        try:
            return current_app.upload_set_config[self.name]
        except AttributeError:
            raise RuntimeError("cannot access configuration outside request")
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    def url(self, filename):
        """
        This function gets the URL a file uploaded to this set would be
        accessed at. It doesn't check whether said file exists.
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
        :param filename: The filename to return the URL for.
        """
        base = self.config.base_url
        if base is None:
            return url_for('_uploads.uploaded_file', setname=self.name,
                           filename=filename, _external=True)
        else:
            return base + filename
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    def path(self, filename, folder=None):
        """
        This returns the absolute path of a file uploaded to this set. It
        doesn't actually check whether said file exists.
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
        :param filename: The filename to return the path for.
        :param folder: The subfolder within the upload set previously used
                       to save to.
        """
        if folder is not None:
            target_folder = os.path.join(self.config.destination, folder)
        else:
            target_folder = self.config.destination
        return os.path.join(target_folder, filename)
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    def file_allowed(self, storage, basename):
        """
        This tells whether a file is allowed. It should return `True` if the
        given `werkzeug.FileStorage` object can be saved with the given
        basename, and `False` if it can't. The default implementation just
        checks the extension, so you can override this if you want.
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
        :param storage: The `werkzeug.FileStorage` to check.
        :param basename: The basename it will be saved under.
        """
        return self.extension_allowed(extension(basename))
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    def extension_allowed(self, ext):
        """
        This determines whether a specific extension is allowed. It is called
        by `file_allowed`, so if you override that but still want to check
        extensions, call back into this.
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
        :param ext: The extension to check, without the dot.
        """
        return ((ext in self.config.allow) or
                (ext in self.extensions and ext not in self.config.deny))
<<<<<<< HEAD
    def get_basename(self, filename):
        return lowercase_ext(secure_filename(filename))
=======

    def get_basename(self, filename):
        return lowercase_ext(secure_filename(filename))

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    def save(self, storage, folder=None, name=None):
        """
        This saves a `werkzeug.FileStorage` into this upload set. If the
        upload is not allowed, an `UploadNotAllowed` error will be raised.
        Otherwise, the file will be saved and its name (including the folder)
        will be returned.
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
        :param storage: The uploaded file to save.
        :param folder: The subfolder within the upload set to save to.
        :param name: The name to save the file as. If it ends with a dot, the
                     file's extension will be appended to the end. (If you
                     are using `name`, you can include the folder in the
                     `name` instead of explicitly using `folder`, i.e.
                     ``uset.save(file, name="someguy/photo_123.")``
        """
        if not isinstance(storage, FileStorage):
            raise TypeError("storage must be a werkzeug.FileStorage")
<<<<<<< HEAD
        if folder is None and name is not None and "/" in name:
            folder, name = os.path.split(name)
=======

        if folder is None and name is not None and "/" in name:
            folder, name = os.path.split(name)

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
        basename = self.get_basename(storage.filename)
        if name:
            if name.endswith('.'):
                basename = name + extension(basename)
            else:
                basename = name
<<<<<<< HEAD
        if not self.file_allowed(storage, basename):
            raise UploadNotAllowed()
=======

        if not self.file_allowed(storage, basename):
            raise UploadNotAllowed()

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
        if folder:
            target_folder = os.path.join(self.config.destination, folder)
        else:
            target_folder = self.config.destination
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        if os.path.exists(os.path.join(target_folder, basename)):
            basename = self.resolve_conflict(target_folder, basename)
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
        target = os.path.join(target_folder, basename)
        storage.save(target)
        if folder:
            return posixpath.join(folder, basename)
        else:
            return basename
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    def resolve_conflict(self, target_folder, basename):
        """
        If a file with the selected name already exists in the target folder,
        this method is called to resolve the conflict. It should return a new
        basename for the file.
<<<<<<< HEAD
        The default implementation splits the name and extension and adds a
        suffix to the name consisting of an underscore and a number, and tries
        that until it finds one that doesn't exist.
=======

        The default implementation splits the name and extension and adds a
        suffix to the name consisting of an underscore and a number, and tries
        that until it finds one that doesn't exist.

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
        :param target_folder: The absolute path to the target.
        :param basename: The file's original basename.
        """
        name, ext = os.path.splitext(basename)
        count = 0
        while True:
            count = count + 1
            newname = '%s_%d%s' % (name, count, ext)
            if not os.path.exists(os.path.join(target_folder, newname)):
                return newname
<<<<<<< HEAD
uploads_mod = Blueprint('_uploads', __name__, url_prefix='/_uploads')
=======


uploads_mod = Blueprint('_uploads', __name__, url_prefix='/_uploads')


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
@uploads_mod.route('/<setname>/<path:filename>')
def uploaded_file(setname, filename):
    config = current_app.upload_set_config.get(setname)
    if config is None:
        abort(404)
    return send_from_directory(config.destination, filename)
<<<<<<< HEAD
=======


>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
class TestingFileStorage(FileStorage):
    """
    This is a helper for testing upload behavior in your application. You
    can manually create it, and its save method is overloaded to set `saved`
    to the name of the file it was saved to. All of these parameters are
    optional, so only bother setting the ones relevant to your application.
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    :param stream: A stream. The default is an empty stream.
    :param filename: The filename uploaded from the client. The default is the
                     stream's name.
    :param name: The name of the form field it was loaded from. The default is
                 `None`.
    :param content_type: The content type it was uploaded as. The default is
                         ``application/octet-stream``.
    :param content_length: How long it is. The default is -1.
    :param headers: Multipart headers as a `werkzeug.Headers`. The default is
                    `None`.
    """
    def __init__(self, stream=None, filename=None, name=None,
                 content_type='application/octet-stream', content_length=-1,
                 headers=None):
        FileStorage.__init__(self, stream, filename, name=name,
            content_type=content_type, content_length=content_length,
            headers=None)
        self.saved = None
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
    def save(self, dst, buffer_size=16384):
        """
        This marks the file as saved by setting the `saved` attribute to the
        name of the file it was saved to.
<<<<<<< HEAD
=======

>>>>>>> 69891c99972d5694a50e4c8d6c6dee600ce24345
        :param dst: The file to save to.
        :param buffer_size: Ignored.
        """
        if isinstance(dst, string_types):
            self.saved = dst
        else:
            self.saved = dst.name
