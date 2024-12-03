VSCODE_FILE = """
{
	"$schema": "https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json",
	"name": "Xenon",
	"patterns": [
		{"include": "#comments"},
		{"include": "#strings"},
		{"include": "#numbers"},
		{"include": "#keywords"},
		{"include": "#types"},
		{"include": "#functions"},
		{"include": "#operators"},
		{"include": "#literals"},
		{"include": "#variables"}
	],
	"repository": {
		"comments": {
			"patterns": [
				{
					"name":"comment.line.double-slash.xenon",
					"begin": "%(LINE_COMMENT_BEGIN)s",
					"beginCaptures": {
						"0": { "name": "punctuation.definition.comment.xenon" }
					},
					"end": "%(LINE_COMMENT_END)s"
				},
				{
					"name": "comment.block.gladoslang",
					"begin": "%(BLOCK_COMMENT_BEGIN)s",
					"beginCaptures": {
					  "0": { "name": "punctuation.definition.comment.begin.gladoslang" }
					},
					"end": "%(BLOCK_COMMENT_END)s",
					"endCaptures": {
					  "0": { "name": "punctuation.definition.comment.end.gladoslang" }
					}
				}
			]
		},
		"strings": {
			"patterns": [
				{
					"name": "string.quoted.double.xenon",
					"begin": "%(STRING_LITERAL)s",
					"end": "%(STRING_LITERAL)s",
					"patterns": [
						{
							"name": "constant.character.escape.xenon",
							"match": "%(ESCAPE_CHAR)s"
						}
					]
				}
			]
		},
		"numbers": {
			"patterns": [
				{
					"name": "constant.numeric.decimal.xenon",
					"match": "%(DECIMAL_NUMBER)s"
				}
			]
		},
		"keywords": {
			"patterns": [
				{
					"name": "keyword.control.xenon",
					"match": "%(KEYWORDS)s"
				}
			]
		},
		"types": {
			"patterns": [
				{
					"name": "storage.type.xenon",
					"begin": "%(TYPE_BEGIN)s",
					"match": "%(TYPE_MATCH)s",
					"end": "%(TYPE_END)s"
				}
			]
		},
		"functions": {
			"patterns": [
				{
					"name": "entity.name.function.call.xenon",
					"match": "%(FUNCTION_CALL)s"
				}
			]
		},
		"operators": {
			"patterns": [
				{
					"name": "keyword.operator.xenon",
					"match": "%(OPERATORS)s"
				}
			]
		},
		"variables": {
			"patterns": [
				{
					"name": "variable.other.gladoslang",
					"match": "%(VARIABLE)s",
					"captures": {
						"0": { "name": "variable.other.gladoslang" }
					}
				}
			]
		},
		"literals": {
			"patterns": [
				{
					"name": "constant.language.gladoslang",
					"match": "%(LITERALS)s"
				}
			]
		}
				
	},
	"scopeName": "source.xn"
}
"""