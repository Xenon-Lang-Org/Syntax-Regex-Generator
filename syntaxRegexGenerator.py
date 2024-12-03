regex_dict = {
"LINE_COMMENT_BEGIN" : "//",
"LINE_COMMENT_END" : "\\n",
"BLOCK_COMMENT_BEGIN" : "/\\\\*",
"BLOCK_COMMENT_END" : "\\\\*/",
"STRING_LITERAL" : "\\\"",
"CHAR_LITERAL" : "'",
"ESCAPE_CHAR" : "\\\\\\\\.",
"DECIMAL_NUMBER" : "\\\\b[0-9]+[.]?[0-9]*\\\\b",
"KEYWORDS" : "\\\\b(let|fn|while|if|elif|else|return|type)\\\\b",
"TYPE_BEGIN" : "(->\\\\s*)?",
"TYPE_MATCH" : ":?\\\\s*(\\\\*?\\\\s*(mut\\\\s+)?)*\\\\b(i8|i16|i32|i64|u8|u16|u32|u64|f32|f64|bool|char|void|[A-Z][a-zA-Z0-9_]*)\\\\b",
"TYPE_END" : ".*",
"FUNCTION_CALL" : "\\\\b([a-zA-Z_][a-zA-Z0-9_]*)\\\\s*\\\\(",
"OPERATORS" : "@|&",
"VARIABLE" : "\\\\b[a-zA-Z_][a-zA-Z0-9_]*\\\\b",
"LITERALS" : "\\\\b(true|false)\\\\b"
}


from vscodeHighlighter import VSCODE_FILE

# save to file truc.txt
with open("xenon.tmLanguage.json", "w") as f:
    f.write(VSCODE_FILE % regex_dict)