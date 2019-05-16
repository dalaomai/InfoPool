create table User(
	id int auto_increment primary key,
    userName char(255) not null unique,
    password char(255) not null,
    permission char(255),
    wechatId char(255) unique,
    wechatName char(255),
    registerTime timestamp default current_timestamp(),
    phoneNumber char(255) unique,
    emailAddress char(255) unique,
    updateTime timestamp default current_timestamp()
);

create table Rule(
	id int auto_increment primary key,
    webName char(255) not null,
    webUrl char(255) not null,
    #alter table rule add column webModel char(255) not null default "normal" after webUrl
    webModel char(255) not null default "normal",
    rulePattern text not null,
    ruleModel char(255) not null,
    titlePosition text not null,
    timePosition text not null,
    hrefPosition text not null,
    isEffect boolean not null default true,	
    updateTime timestamp default current_timestamp()
);
create table Message(
	id int auto_increment primary key,
    title char(255) not null,
    href char(255) not null,
    time char(30) not null,
    ruleId int not null,
    updateTime timestamp default current_timestamp(),

    foreign key(ruleId) references Rule(id)
);
create table User_Rule(
	id int auto_increment primary key,
	userId int,
    ruleId int,
    isPush boolean,
    lastPushTime timestamp default current_timestamp(),
    
    foreign key(userId) references User(id),
    foreign key(ruleId) references Rule(id),
    updateTime timestamp default current_timestamp()
);


create view UnPushed as
select User.id userId,wechatId,Rule.id ruleId,webName,webUrl,title,href,time,lastPushTime
from  User,Rule,Message,User_Rule
where User_Rule.ruleId = Message.ruleId and User_Rule.lastPushTime < Message.updateTime and User_Rule.isPush=true;

#INSERT INTO rule (`id`, `webName`, `webUrl`, `rulePattern`, `ruleModel`, `titlePosition`, `timePosition`, `hrefPosition`, `isEffect`) 
#VALUES ('1', '佛山市人民政府', 'http://www.foshan.gov.cn/zwgk/zwdt/jryw/', '<li [\\s\\S]*?([0-9]{4}-[0-9]{2}-[0-9]{2})[\\s\\S]*?href=\"([\\s\\S]*?)\"[\\s\\S]*?title=\"([\\s\\S]*?)\" >', 'regular', '2', '0', '1', '1');

