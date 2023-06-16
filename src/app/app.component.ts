import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  isconcept: string = '';
  species: string = '';
  sex: string = '';
  age: string = '';
  physicalShape: string = '';
  hairColor: string = ''
  eyes: string = ''
  mainColors: string = '';
  deformation: string = '';
  skillsPowers: string = '';
  clothing: string = '';
  contextUniverse: string = '';
  socialContext: string = '';
  occupationProfession: string = '';
  ethnicity: string = '';
  personalityTraits: string = '';
  artstyleInspiration: string = '';
  extras: string = '';
  image: string | undefined;
  image2: string | undefined;
  prompts: string[] = [];
  

  constructor(private http: HttpClient) {}

  generateImage() {
    // Combine all the category values into one prompt string
    const prompt = `${this.species}\n${this.sex}\n${this.age}\n${this.physicalShape}\n${this.hairColor}\n${this.eyes}\n${this.mainColors}\n${this.deformation}\n${this.skillsPowers}\n${this.clothing}\n${this.contextUniverse}\n${this.socialContext}\n${this.occupationProfession}\n${this.ethnicity}\n${this.personalityTraits}\n${this.artstyleInspiration}\n${this.extras}`;
    
    this.http.post<any>('http://localhost:5000/generate-image', { prompt: prompt })
      .subscribe(res => {
        this.image = 'data:image/png;base64,' + res.image;
        this.image2 = 'data:image/png;base64,' + res.image2;
        console.log(res.prompts); 
        this.prompts = res.prompts; 
      }, err => {
        console.log(err);
      });
  }
}