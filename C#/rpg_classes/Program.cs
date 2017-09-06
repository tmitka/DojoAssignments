using System;

namespace rpg_classes
{
    class Program
    {
        static void Main(string[] args)
        {
            Human person = new Human("Ted");
            Console.WriteLine(person.name);
            Wizard wizard = new Wizard();
            Console.WriteLine(wizard.name);
            Console.WriteLine(wizard.health);
            Console.WriteLine(wizard.strength);
            Console.WriteLine(wizard.intelligence);
            wizard.heal();
            Console.WriteLine(wizard.health);
        }
    }
}
