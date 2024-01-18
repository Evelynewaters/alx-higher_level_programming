-- It creates database hbtn_0d_2 + a user to control it, both if not already existing
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2. * TO user_0d_2@localhost;
