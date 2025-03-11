import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ProfileController } from './profile/profile.controller';

@Module({
  imports: [],
  controllers: [AppController, ProfileController],
  providers: [AppService],
})
export class AppModule {}
