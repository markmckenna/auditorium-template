# Auditorium Slide Presentation Template Repository

This can be cloned and used as the basis of an Auditorium-based slide presentation that renders in a locally hosted browser pushing out moment.js.

## Usage:

```
git clone git@github.com:markmckenna/auditorium-template.git
cd auditorium-template
./install.sh
```

If the install went well, the demo slideshow should be hosted locally, viewable in a browser. The demo slideshow contains basic instructions on how to make a presentation.

Your own slideshow can be run with `./start.sh`, which will use `index.py` as the script supporting the slide show.

Note that this uses a local Python environment based on Python 3.8, using pinned versions of specific dependencies required for the (now-defunct) Auditorium project to function. To play around with this repo properly from the command line, you'll need to run

```
source .env/bin/activate
```

to inject the Python environment into your local shell. VS Code should (hopefully?) do this automatically with the Python plugin, but I haven't seen that work yet. The shell scripts do this for themselves, but that doesn't carry over to your own interactive shell.

To get back out of the Python environment just type `deactivate`.