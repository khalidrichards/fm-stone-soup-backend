import { Controller, Get } from '@nestjs/common';

@Controller('profile')
export class ProfileController {

    @Get()
    getAllProfiles(): string {
        return 'Soon, we will see Q and Gen and Melanie and Crystal and Khalid';
    }
}
