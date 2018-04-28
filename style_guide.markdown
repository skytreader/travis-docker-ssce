# Style Guide

I am writing this more as a reference for refactoring than an intro guide.
Whatever I have now does not have that much guidance when it comes to style,
unfortunately.

## HTML

Use `snake-case` but with dashes instead of underscores since it is faster to
type (no need to hold down shift) for identifiers

## CSS

Use `snake-case` but with dashes instead of underscores since it is faster to
type (no need to hold down shift) for identifiers

## JavaScript

Refer to [Google's style guide](https://google.github.io/styleguide/javascriptguide.xml).
Some specifics and/or deviations below. Document assumes that jQuery is used.
Where Google's and this document diverges, this document prevails.

All event handlers should be bound in the `$(document).ready` of the script. The
idea is that if you want to rewrite the frontend, you just need to create a new
template (following the assumptions of the script regarding element identifiers
and structure) and the script should still be mostly compatible with it.

Documentation uses [JSDoc](http://usejsdoc.org/). The declarable types are
JavaScript natives and [Mozilla Web API types](https://developer.mozilla.org/en-US/docs/Web/API).

Use `camelCasing` as opposed to `snake_case`. `SHOUT_FOR_CONSTANTS`. A possible
exception is if a particular data/field comes from a server query in which case
`snake_case` should be acceptable.

### Other Related Links:

1. [Google: Anotating JavaScript for the Closure Compiler](https://developers.google.com/closure/compiler/docs/js-for-compiler)

## Python

Follow [PEP8](https://www.python.org/dev/peps/pep-0008/).

### SQLAlchemy

Always explicitly name foreign key constraints so that they are easily referred
to in migrations.

All foreign key references should, as much as possible, be named as
`<table-name>_<foreign-field>`. Sometimes, using the table name is not feasible
as one table may FK to another table more than once. In this case, be descriptive.
The hard rule is that it should end with the foreign field it is using as FK.

Foreign key fields should have a corresponding field in the model declared as
a [relationship](http://docs.sqlalchemy.org/en/latest/orm/relationships.html).
Note that, using this stack's `UserTaggedBase`, you have to explicitly declare
the following fields in the classes inheriting from `UserTaggedBase`

    class Example(UserTaggedBase):
        ...
        creator = relationship("User", foreign_keys="Example.creator_id")
        last_modifier = relationship("User", foreign_keys="Example.last_modifier_id")

When declaring columns, explicitly specify both `default` and `server_default`.
The difference is that `default` is the value _Python_ automagically encounters
while `server_default` is the value _the database_ automagically sets.
