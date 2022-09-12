import json

import idom


mui = idom.web.module_from_template(
    "react@^17.0.0",
    "@material-ui/core@4.12.4",
    fallback="⌛",
)
Button = idom.web.export(mui, "Button")


@idom.component
def ViewButtonEvents():
    event, set_event = idom.hooks.use_state(None)

    return idom.html.div(
        Button(
            {
                "color": "primary",
                "variant": "contained",
                "onClick": lambda event: set_event(event),
            },
            "Click Me!",
        ),
        idom.html.pre(json.dumps(event, indent=2)),
    )


idom.run(ViewButtonEvents)