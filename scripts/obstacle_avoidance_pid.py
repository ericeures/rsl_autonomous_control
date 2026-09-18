#!/usr/bin/env python3
"""
RobotiqueStudio Labs (RSL) - Autonomous Control Script
Description: Differential drive robot obstacle avoidance using a basic Proportional feedback loop.
Compatible with Webots Robot API.
"""

from controller import Robot

class RSLAutonomousController:
    def __init__(self):
        # Initialisation de l'instance du robot Webots
        self.robot = Robot()
        self.time_step = int(self.robot.getBasicTimeStep())
        
        # Vitesse maximale des moteurs
        self.max_speed = 6.28
        
        # Configuration des moteurs du robot différentiel
        self.left_motor = self.robot.getDevice('left wheel motor')
        self.right_motor = self.robot.getDevice('right wheel motor')
        self.left_motor.setPosition(float('inf'))
        self.right_motor.setPosition(float('inf'))
        self.left_motor.setVelocity(0.0)
        self.right_motor.setVelocity(0.0)
        
        # Configuration des capteurs de proximité (Exemple pour Pioneer ou e-puck)
        self.sensors = []
        self.sensor_names = ['ps0', 'ps1', 'ps7'] # Capteurs orientés vers l'avant
        for name in self.sensor_names:
            sensor = self.robot.getDevice(name)
            sensor.enable(self.time_step)
            self.sensors.append(sensor)

    def run_control_loop(self):
        # Boucle de contrôle principale
        while self.robot.step(self.time_step) != -1:
            # Lecture des valeurs des capteurs (Feedback)
            sensor_values = [sensor.getValue() for sensor in self.sensors]
            
            # Loi de commande Proportionnelle (P) simple pour l'évitement d'obstacles
            obstacle_detected = any(val > 80.0 for val in sensor_values)
            
            if obstacle_detected:
                # Réponse proportionnelle : Rotation du robot pour éviter la collision
                left_speed  = -0.5 * self.max_speed
                right_speed =  0.5 * self.max_speed
            else:
                # Vitesse de croisière en ligne droite si la voie est libre
                left_speed  = 0.7 * self.max_speed
                right_speed = 0.7 * self.max_speed
                
            # Envoi des commandes aux actionneurs
            self.left_motor.setVelocity(left_speed)
            self.right_motor.setVelocity(right_speed)

if __name__ == '__main__':
    # Instanciation et lancement du contrôle de navigation autonome RSL
    controller = RSLAutonomousController()
    controller.run_control_loop()
