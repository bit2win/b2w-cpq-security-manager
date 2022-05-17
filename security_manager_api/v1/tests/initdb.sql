CREATE TABLE fields (
	id INTEGER NOT NULL primary key,
	guid char(36) NOT NULL default (
	    lower(hex(randomblob(4))) || '-' || lower(hex(randomblob(2))) || '-4' || substr(lower(hex(randomblob(2))),2) ||
	     '-' || substr('89ab',abs(random()) % 4 + 1, 1) || substr(lower(hex(randomblob(2))),2) || '-'
	     || lower(hex(randomblob(6)))),
	created_date DATETIME NOT NULL default (DATETIME('now')),
	update_date DATETIME NOT NULL default (DATETIME('now')),
	field_name varchar(50) NOT NULL,
	field_type varchar(255) NOT NULL,
	default_value varchar(255) NULL,
	field_precision INTEGER NULL,
	field_scale INTEGER NULL,
	field_enum text NULL,
	field_pattern varchar(255) NULL,
	max_length INTEGER NULL,
	string_length INTEGER NULL,
	fk_table varchar(255) NULL,
	required_field INTEGER NULL DEFAULT 0,
	system_field INTEGER NULL DEFAULT 0,
	objects_guid int4 NULL
);

CREATE TABLE objects(
	id INTEGER NOT NULL PRIMARY KEY,
	guid char(36) NOT NULL default (
	    lower(hex(randomblob(4))) || '-' || lower(hex(randomblob(2))) || '-4' || substr(lower(hex(randomblob(2))),2) ||
	     '-' || substr('89ab',abs(random()) % 4 + 1, 1) || substr(lower(hex(randomblob(2))),2) || '-'
	     || lower(hex(randomblob(6)))),
	table_name varchar(253) NOT NULL unique,
	created_date DATETIME NOT NULL default (DATETIME('now')),
	update_date DATETIME NOT NULL default (DATETIME('now')),
	system_table INTEGER NOT NULL DEFAULT 0,
	is_m2m INTEGER NOT NULL DEFAULT 0
);

