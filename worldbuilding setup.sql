create database worldbuilding;

use worldbuilding;

create table Species (
scientificname varchar(200) not null,
speciesdescription mediumtext,
primary key (scientificname)
);

create table Characters (
characterid int not null auto_increment,
species varchar(200),
sex varchar(200),
height float,
weight float,
primary key (characterid),
foreign key (species) references Species(scientificname) ON DELETE SET NULL ON UPDATE Cascade
);

create table SignificantCharacters (
characterid int not null,
firstname varchar(200),
familyname varchar(200),
alias varchar(200),
age int,
occupation varchar(200),
characterdescription mediumtext,
primary key (characterid),
foreign key (characterid) references Characters(characterid)
);

delimiter //
CREATE function characterExtendable (id INT)
returns boolean reads sql data
BEGIN
return (exists(select characterid from characters where id = characterid)) and 
(not exists(select characterid from significantcharacters where id = characterid));
END//

delimiter //
CREATE function characterExists (id INT)
returns boolean reads sql data
BEGIN
return exists(select characterid from characters where id = characterid);
END//

delimiter //
CREATE function isSignificant (id INT)
returns boolean reads sql data
BEGIN
return exists(select characterid from significantcharacters where id = characterid);
END//

CREATE function isSpecies (speciesName varchar(200))
returns boolean reads sql data
BEGIN
return exists(select * from species where scientificname = speciesName);
END//

create procedure ResetPopulation () MODIFIES SQL DATA
begin
SET SQL_SAFE_UPDATES = 0;
delete from characters where not isSignificant(characterid);
SET SQL_SAFE_UPDATES = 1;
end//

delimiter ;