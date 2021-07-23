<template>
<div>
    <v-navigation-drawer
            v-model="drawer"
            temporary
            app
            dark
            color="black"
            style="z-index:11;"
        >        
        <v-list dense nav>

            <v-list-item link :href="routes.visit">
                <v-list-item-content>
                        <a  class="my-2 text-lg no-underline p-3 w-2/12 text-white " :href="routes.visit">
                            <div class="mr-text">Toru Mai</div>
                            <div class="eng-text">Visit</div>
                        </a>
                </v-list-item-content>
            </v-list-item>
            <v-list-item link :href="routes.discover">
                <v-list-item-content>
                    <a  class="my-2 text-lg no-underline p-3 w-2/12 text-white " :href="routes.discover">
                        <div class="mr-text">Toru Mai</div>
                        <div class="eng-text">Discover</div>
                    </a>
                </v-list-item-content>
            </v-list-item>
            <v-list-item link :href="routes.war">
                <v-list-item-content>
                        <a  class="my-2 text-lg no-underline p-3 w-2/12 text-white " :href="routes.war">
                            <div class="mr-text">Paenga Hira</div>
                            <div class="eng-text">War Memorial</div>
                        </a>
                </v-list-item-content>
            </v-list-item>
            <v-list-item link :href="routes.museum">
                <v-list-item-content>
                    <a  class="my-2 text-lg no-underline p-3 w-2/12 text-white " :href="routes.museum">
                        <div class="mr-text">Tō Whare Taonga</div>
                        <div class="eng-text">Your museum</div>
                    </a>
                </v-list-item-content>
            </v-list-item>
            <v-list-item link :href="routes.learn">
                <v-list-item-content>
                    <a  class="my-2 text-lg no-underline p-3 w-2/12 text-white " :href="routes.learn">
                        <div class="mr-text">Ako</div>
                        <div class="eng-text">Learn</div>
                    </a>
                </v-list-item-content>
            </v-list-item>
            

        </v-list>
        <v-divider></v-divider>
        
    </v-navigation-drawer>


    <div class="navbar fixed z-10">
        <div class="clearfix bg-black text-white hidden-sm-and-down">
            <div class="float-right donate-links">
                <a class="p-2 text-white no-underline dlink" href="https://www.aucklandmuseum.com/visit/tickets">TICKETS</a>
                <a class="p-2 text-white no-underline dlink" href="https://www.aucklandmuseum.com/your-museum/support-your-museum/donate">DONATE</a>
            </div>
        </div>
        <div class="text-white bg-black">
            <div class="container  flex justify-between">
                <div class="lg:w-2/12 w-8/12 ">
                    <h2 class="p-1 flex" >
                    <a href="/" class="no-underline text-white flex">
                            <img class="logo" src="/static/imgs/mlogo.svg" alt="">
                        </a>
                        
                    </h2>

                </div>
                <span @click="navdrawerToggle" class="menu-btn hidden-md-and-up mr-4 w-1/12">
                    <div class="small-line-menu med"></div>
                    <div class="small-line-menu med"></div>
                    <div class="small-line-menu med "></div>
                </span>
                <div class="w-10/12 hidden-sm-and-down">
                    <div class="flex items-baseline justify-around">
                        <a  class="nav-link my-2 text-lg no-underline p-3 w-2/12 text-white " :href="routes.visit">
                            <div class="mr-text">Toru Mai</div>
                            <div class="eng-text">Visit</div>
                        </a>
                        <a  class="nav-link my-2 text-lg no-underline p-3 w-2/12 text-white " :href="routes.discover">
                            <div class="mr-text">Toru Mai</div>
                            <div class="eng-text">Discover</div>
                        </a>
                        <a  class="nav-link my-2 text-lg no-underline p-3 w-2/12 text-white " :href="routes.learn">
                            <div class="mr-text">Ako</div>
                            <div class="eng-text">Learn</div>
                        </a>
                        <a  class="nav-link my-2 text-lg no-underline p-3 w-2/12 text-white " :href="routes.war">
                            <div class="mr-text">Paenga Hira</div>
                            <div class="eng-text">War Memorial</div>
                        </a>
                        <a  class="nav-link my-2 text-lg no-underline p-3 w-2/12 text-white " :href="routes.museum">
                            <div class="mr-text">Tō Whare Taonga</div>
                            <div class="eng-text">Your museum</div>
                        </a>
                        

                    </div>
                </div>
            </div>

        </div>
    </div>
    <br>
    <br>
</div>
</template>
<script>
import { mdiMenu } from '@mdi/js'; 
import routes from '../routes';
export default {
    props:{
        activeLink:{default:8},
    },
    data(){
        return{
            hoverMenu:false,
            menuIcon:mdiMenu,
            drawer:false,
            csrf:"",
            loggedIn:"",
            routes:routes,

        }
    },methods:{
        navdrawerToggle(){
            this.drawer = !this.drawer    
        }
    }
}
</script>
<style>
.mr-text{
    font-weight: 300;
}

.eng-text{
    font-weight: 500;
}

@media only screen and ( max-width: 1262px) and (min-width: 1024px){

    .logo{
        position: relative;
        left: -1px;
        bottom: -73px;
        display: inline-block;
        background-color: #000;
    }
}

@media only screen and ( min-width: 1262px){

    .logo{
        position: relative;
        left: -1px;
        bottom: -52px;
        display: inline-block;
        background-color: #000;
    }
}

@media only screen and ( max-width: 1024px){

    .logo{
        position: relative;
        left: -1px;
        bottom: -23px;
        display: inline-block;
        background-color: #000;
    }
}


.nav-link:hover{
    border-bottom: 2px solid white;
}

.menu-btn{
    margin-top: 5px;
    cursor: pointer;
    width: 40px;
}
.small-line-menu{
    width:20px;
    height: 5px;
    background: #888888e8;
    margin-bottom: 4px;
    border-radius: 2px;
}
.small-line-menu.up{
    width:40px;
    transition: 300ms;
}
.small-line-menu.med{
    width:30px;
}
.small-line-menu.low{
    transition: 300ms;
    width:20px;
}

.donate-links{
    padding: 5px;
    margin: 10px;
}

.dlink{
    border: solid #ccc 0.1px;
}

.navbar{
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    width:100%;
    border-bottom: 8px white solid;
}

.img-logo{   
    height: 50px;
    width: 50px;
}
.slide-bg-hover {
    background-size: 200% 100%;
    background-image: linear-gradient(to right,  black 50%, white 50%);
    transition: 500ms;
    font-family: 'Righteous';
}

.slide-bg-hover:hover {

    background-position: +100% 00;
    color: black;
}
.small-line-menu{
    width:20px;
    height: 5px;
    background: white;
    margin-bottom: 4px;
    border-radius: 2px;
}
.bug{
    margin-top: 4px;
}
</style>