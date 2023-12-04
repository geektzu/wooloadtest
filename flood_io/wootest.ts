import { step, By, Until } from "@flood/element";

export const settings: TestSettings = {
  loopCount: -1,
  description: "Woo Store Test",
  screenshotOnFailure: true,
  disableCache: true,
  clearCache: true,
  clearCookies: true,
  actionDelay: 1.5,
  stepDelay: 2.5,
};

var nameList = [
                'Time','Past','Future','Dev',
                'Fly','Flying','Soar','Soaring','Power','Falling',
                'Fall','Jump','Cliff','Mountain','Rend','Red','Blue',
                'Green','Yellow','Gold','Demon','Demonic','Panda','Cat',
                'Kitty','Kitten','Zero','Memory','Trooper','XX','Bandit',
                'Fear','Light','Glow','Tread','Deep','Deeper','Deepest',
                'Mine','Your','Worst','Enemy','Hostile','Force','Video',
                'Game','Donkey','Mule','Colt','Cult','Cultist','Magnum',
                'Gun','Assault','Recon','Trap','Trapper','Redeem','Code',
                'Script','Writer','Near','Close','Open','Cube','Circle',
                'Geo','Genome','Germ','Spaz','Shot','Echo','Beta','Alpha',
                'Gamma','Omega','Seal','Squid','Money','Cash','Lord','King',
                'Duke','Rest','Fire','Flame','Morrow','Break','Breaker','Numb',
                'Ice','Cold','Rotten','Sick','Sickly','Janitor','Camel','Rooster',
                'Sand','Desert','Dessert','Hurdle','Racer','Eraser','Erase','Big',
                'Small','Short','Tall','Sith','Bounty','Hunter','Cracked','Broken',
                'Sad','Happy','Joy','Joyful','Crimson','Destiny','Deceit','Lies',
                'Lie','Honest','Destined','Bloxxer','Hawk','Eagle','Hawker','Walker',
                'Zombie','Sarge','Capt','Captain','Punch','One','Two','Uno','Slice',
                'Slash','Melt','Melted','Melting','Fell','Wolf','Hound',
                'Legacy','Sharp','Dead','Mew','Chuckle','Bubba','Bubble','Sandwich','Smasher','Extreme','Multi','Universe','Ultimate','Death','Ready','Monkey','Elevator','Wrench','Grease','Head','Theme','Grand','Cool','Kid','Boy','Girl','Vortex','Paradox'
            ];
        
var finalName = ""

function generate() {
   var finalName = nameList[Math.floor( Math.random() * nameList.length )];
   return finalName;
};

export default () => {
  step("Add to cart", async (browser) => {
    await browser.visit("https://loadtest.mystagingwebsite.com/chairs/daily-chair.html/");
    let cart = await browser.findElement(By.css("button[name='add-to-cart']"));
    await cart.click();
  });

  step("Checkout", async (browser) => {
    await browser.visit("https://loadtest.mystagingwebsite.com/checkout-2");
    await browser.type(By.id("billing_first_name"), generate());
    await browser.type(By.id("billing_last_name"), generate());
    await browser.type(By.id("billing_address_1"), '60 29th Street #343');
    await browser.type(By.id("billing_city"), 'San Francisco');
    await browser.type(By.id("billing_postcode"), '94110');
    await browser.type(By.id("billing_phone"), '08002733049');
    await browser.type(By.id("billing_email"), 'alan.zhutao@gmail.com');
    let co = await browser.findElement(By.css("button[name='woocommerce_checkout_place_order']"));
    await co.click();
   
  });

  
};