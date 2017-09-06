using System;
using System.Collections.Generic;

namespace rpg_classes{
    public class Human{
        public string name;

        public int health { get; set; }
        public int strength {get; set; }
        public int intelligence {get; set; }
        public int dexterity {get; set; }

        public Human(string person){
            name = person;
            strength = 3;
            intelligence = 3;
            dexterity = 3;
            health = 100;
        }
        public void attack(object obj){
            Human enemy = obj as Human;
            if(enemy == null){
                Console.WriteLine("Failed Attack");
            }
            else {
                enemy.health -= strength * 5;
            }
        }
    }
    public class Wizard : Human {
        public Wizard() : base("Gandalf"){
            health = 50;
            intelligence =25;
        }
        public void heal(){
            health += 10;
        }
        public void fireball(object obj){
            Human enemy = obj as Human;
            Random rnd = new Random();
            enemy.health -= rnd.Next(20, 50);;
        }
    }
    public class Ninja : Human {
        public Ninja() : base("Shadow"){
            dexterity = 175;
        }
        public void steal(){
            health += 10;
        }
        public void get_away(){
            health -= 15;
        }
    }
    public class Samurai : Human {
        public Samurai() : base("Sam"){
            health = 200;
        }
        public void death_blow(object obj){
            Human enemy = obj as Human;
            if (enemy.health < 50){
                enemy.health = 0;
            }
            else {
                Console.WriteLine("Death Blow Failed");
            }
        }
        public void meditate(){
            health = 200;
        }
    }
}