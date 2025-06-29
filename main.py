from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)


BASE_DATA_DIR = "/home/alex/Downloads/"


def safe_join(base, *paths):
    """Prevent directory traversal attacks"""
    final_path = os.path.abspath(os.path.join(base, *paths))
    if not final_path.startswith(os.path.abspath(base)):
        abort(403)
    return final_path


@app.route("/", defaults={'subpath': ''})
@app.route("/<path:subpath>")
def browse(subpath):
    full_path = safe_join(BASE_DATA_DIR, subpath)
    if not os.path.exists(full_path):
        abort(404)

    if os.path.isfile(full_path):
        dir_path = os.path.dirname(full_path)
        filename = os.path.basename(full_path)
        return send_from_directory(dir_path, filename)

    # Build listing for directory
    entries = []
    for entry in sorted(os.listdir(full_path)):
        entry_path = os.path.join(full_path, entry)
        is_dir = os.path.isdir(entry_path)
        web_path = os.path.join("/", subpath, entry)
        entries.append((entry, web_path, is_dir))

    # Determine if a parent link should be shown (i.e. are we at the base of the tree?)
    parent_link = None
    if subpath:
        parent_link = "/" + os.path.dirname(subpath.rstrip('/'))

    return render_template(
        template_name_or_list='index.html',
        current_directory="/" + subpath,
        entries=entries,
        parent_link=parent_link,
        website_title='Mock Website: NASA AIA Synoptic'
    )


if __name__ == "__main__":
    app.run(debug=True)
