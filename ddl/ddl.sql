-- ユーザー管理テーブル
DROP TABLE if EXISTS users;
CREATE TABLE users (
    id         INT           NOT NULL   AUTO_INCREMENT   COMMENT 'ID',
    user_name       VARCHAR(32)   NOT NULL                    COMMENT '名前',
    affiliaton VARCHAR(32)                               COMMENT '所属',
    PRIMARY KEY(id)
)COMMENT = 'ユーザ管理テーブル';

-- カテゴリー管理テーブル
DROP TABLE if EXISTS categories;
CREATE TABLE categories (
    id             INT          NOT NULL   AUTO_INCREMENT   COMMENT 'ID',
    user_id        INT          NOT NULL                    COMMENT 'ユーザーID',
    category_name  VARCHAR(32)  NOT NULL                    COMMENT 'カテゴリー名',
    PRIMARY KEY(id),
    UNIQUE (user_id, category_name)
) COMMENT = 'カテゴリー管理テーブル';

-- 勉強記録テーブル
DROP TABLE if EXISTS study_records;
CREATE TABLE study_records(
    id           INT      NOT NULL  AUTO_INCREMENT   COMMENT 'ID',
    user_id      INT      NOT NULL                   COMMENT 'ユーザーID',
    category_id  INT      NOT NULL  DEFAULT 0        COMMENT 'カテゴリーID',
    study_date   DATE     NOT NULL                   COMMENT '勉強日付',
    study_time   TIME     NOT NULL                   COMMENT '勉強時間',
    PRIMARY KEY(id)
)COMMENT = '勉強記録テーブル';

-- 勉強中の学生テーブル
DROP TABLE if EXISTS studying_users;
CREATE TABLE studying_users(
    user_id        INT    NOT NULL      COMMENT 'ユーザーID',
    category_id    INT    NOT NULL      COMMENT 'カテゴリーID',
    start_time     DATETIME   NOT NULL      COMMENT '勉強開始時間',
    PRIMARY KEY(user_id)
)COMMENT = '勉強中の学生テーブル';


-- 外部キー設定
-- カテゴリーテーブルの外部キー
ALTER TABLE categories ADD constraint categories_FK1
    Foreign Key (user_id) REFERENCES users(id);

-- 勉強記録テーブルの外部キー
ALTER TABLE study_records ADD constraint study_records_FK1
    Foreign Key (user_id) REFERENCES users(id);


-- 勉強中の学生テーブルの外部キー
ALTER TABLE studying_users ADD constraint studying_users_FK1
    Foreign Key (user_id) REFERENCES users(id);
ALTER TABLE studying_users ADD constraint studying_users_FK2
    Foreign Key (category_id) REFERENCES categories(id);

INSERT INTO users (id, user_name) VALUES (1, 'その他用');
INSERT INTO categories (id, user_id, category_name) VALUES (1, 1, 'その他');