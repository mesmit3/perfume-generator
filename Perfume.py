# Choosing a random perfume to wear. 
import random

list_hex = ["DTF", "Would Thou Like the Taste of Butter", "Loup-Garou", "Bah, Humbug!", "The Bell Witch", "Brightening the Daybreak", "Embalming Fluid", "Laudanum", "Just Took a DNA Test", "Laundromat", "Leopardite", "Smoky Quartz", "Trashcan Man", "Waking the Witch", "Graveyard", "Thè Noir", "That Fancy Wine", "Tomatè", "Ambre d'Or", "Blue Moon", "Unbaptism", "Bisou", "Witchboard", "Alexandrite", "Cetalox", "Desert Rain", "Fluorite", "Hexenhaus", "Pearanormal Activity", "Reefer Madness", "l'air en hiver", "Le Chat Noir", "Hecate", "Norman Loves Mother", "Thanatos", "Krampusnacht", "Elemental", "Mephistopheles", "White Amber", "Necromancer"]
list_pine = ["Auntumnal", "Eldritch", "Apple Tabac", "Fanghorn", "Glühwein", "oxylus", "Bindebole", "Steading", "Boreal", "Murkwood", "Christmas Wine"]
list_cocoapink = ["Opera Ghost", "Handbook for the Recently Deceased", "Fauno Obscuro", "Beyond the Goblin City"]
list_astrid = ["Merci no. 29", "the creek flows over me", "when dawn breaks", "basking with lizards", "rattlesnake and hummingbird", "flowers growing"]
list_other = ["Rise", "couer de grenade", "Love Dart", "Smokeable", "Ostara", "Baculum", "The Huntress", "Tramp", "Trollop", "Jezebel", "Grass", "Redcorder Music", "The One Lascivious", "Within a Daze of Passion", "Mercury Retrograde", "Yennefer"] 

seqs = list_hex, list_pine, list_cocoapink, list_astrid, list_other

perfume = random.choice(random.choices(seqs, weights=map(len, seqs))[0])
print(perfume)